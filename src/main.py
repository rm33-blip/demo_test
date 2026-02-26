from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue
from src.utils.config_loader import load_config
from src.config.validation import apply_validation_rules


def process(rows: list, config_path: str = "src/config/default_validations.yml"):
    cfg = load_config(config_path)
    rules = cfg.get("validations", [])

    normalized = []
    for r in rows:
        nr = normalize_row(r)
        apply_validation_rules(nr, rules)
        normalized.append(nr)

    # Deterministic ordering
    normalized = sorted(normalized, key=lambda x: (x.get("customer_id") is None, x.get("customer_id")))

    return aggregate_revenue(normalized)
