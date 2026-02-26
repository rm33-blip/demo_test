from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue
from src.utils.config_loader import load_config
from src.config.validation import apply_validation_rules
from src.utils.logger import log


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
    result = aggregate_revenue(normalized)

    log(f"Completed process(): {result}", request_id=request_id)
    return result
