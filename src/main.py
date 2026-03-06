from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue
from src.utils.config_loader import load_config
from src.config.validation import apply_validation_rules
from src.utils.logger import log, log_structured
from src.engine.kpi_engine import calculate_arpu, calculate_churn_rate
from src.config.schema_versions import validate_schema_version, SchemaVersionError


def _try_compute_kpis(rows: list) -> dict:
    """
    Compute KPIs only when the required inputs are present.
    """
    revenue_total = 0.0
    active_users_total = 0
    lost_users_total = 0
    total_users_total = 0

    has_revenue = False
    has_active_users = False
    has_lost_users = False
    has_total_users = False

    for r in rows:
        if r.get("revenue") is not None:
            revenue_total += float(r["revenue"])
            has_revenue = True

        if r.get("active_users") is not None:
            active_users_total += int(r["active_users"])
            has_active_users = True

        if r.get("lost_users") is not None:
            lost_users_total += int(r["lost_users"])
            has_lost_users = True

        if r.get("total_users") is not None:
            total_users_total += int(r["total_users"])
            has_total_users = True

    kpis = {}

    if has_revenue and has_active_users:
        kpis["arpu"] = calculate_arpu(revenue_total, active_users_total)

    if has_lost_users and has_total_users:
        kpis["churn_rate"] = calculate_churn_rate(lost_users_total, total_users_total)

    return kpis


def process(rows: list, config_path: str = "src/config/default_validations.yml", request_id: str = None):
    log("Starting process()", request_id=request_id)

    cfg = load_config(config_path)
    structured_logs = bool(cfg.get("structured_logs", False))
    fail_on_unexpected_columns = bool(cfg.get("fail_on_unexpected_columns", False))

    schema_version = cfg.get("schema_version", "v1")
    try:
        validate_schema_version(schema_version)
    except SchemaVersionError as e:
        log_structured(
            "Schema version validation failed",
            request_id=request_id,
            fields={"received": schema_version, "supported": ["v1"], "error": str(e)},
            structured=structured_logs,
        )
        raise

    rules = cfg.get("validations", [])
    log_structured(
        "Loaded validation rules",
        request_id=request_id,
        fields={
            "count": len(rules),
            "fail_on_unexpected_columns": fail_on_unexpected_columns,
        },
        structured=structured_logs,
    )

    normalized = []
    for r in rows:
        nr = normalize_row(r, fail_on_unexpected_columns=fail_on_unexpected_columns)
        apply_validation_rules(nr, rules)
        normalized.append(nr)

    normalized = sorted(
        normalized,
        key=lambda x: (
            x.get("revenue") is None,
            -(float(x.get("revenue")) if x.get("revenue") is not None else 0.0),
            x.get("customer_id") is None,
            x.get("customer_id"),
        ),
    )

    agg = aggregate_revenue(normalized)

    kpis = _try_compute_kpis(rows)
    if kpis:
        agg["kpis"] = kpis

    log_structured(
        "Completed process()",
        request_id=request_id,
        fields={"agg": agg},
        structured=structured_logs,
    )
    return agg
