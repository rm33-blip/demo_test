from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue
from src.utils.config_loader import load_config
from src.config.validation import apply_validation_rules
from src.utils.logger import log
from src.engine.kpi_engine import calculate_arpu, calculate_churn_rate


def _try_compute_kpis(rows: list) -> dict:
    """
    Optional KPI computation if inputs exist.
    Uses totals derived from rows if present.
    """
    revenue_total = 0.0
    active_users_total = 0
    lost_users_total = 0
    total_users_total = 0

    any_kpi_inputs = False
    for r in rows:
        if r.get("revenue") is not None:
            revenue_total += float(r["revenue"])
        if r.get("active_users") is not None:
            active_users_total += int(r["active_users"])
            any_kpi_inputs = True
        if r.get("lost_users") is not None:
            lost_users_total += int(r["lost_users"])
            any_kpi_inputs = True
        if r.get("total_users") is not None:
            total_users_total += int(r["total_users"])
            any_kpi_inputs = True

    if not any_kpi_inputs:
        return {}

    return {
        "arpu": calculate_arpu(revenue_total, active_users_total),
        "churn_rate": calculate_churn_rate(lost_users_total, total_users_total),
    }


def process(rows: list, config_path: str = "src/config/default_validations.yml", request_id: str = None):
    log("Starting process()", request_id=request_id)

    cfg = load_config(config_path)
    rules = cfg.get("validations", [])
    log(f"Loaded {len(rules)} validation rules", request_id=request_id)

    normalized = []
    for r in rows:
        nr = normalize_row(r)
        apply_validation_rules(nr, rules)
        normalized.append(nr)

    normalized = sorted(normalized, key=lambda x: (x.get("customer_id") is None, x.get("customer_id")))
    agg = aggregate_revenue(normalized)

    # Optional KPIs
    kpis = _try_compute_kpis(rows)
    if kpis:
        agg["kpis"] = kpis

    log(f"Completed process(): {agg}", request_id=request_id)
    return agg
