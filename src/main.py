from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue


def process(rows: list):
    normalized = [normalize_row(r) for r in rows]
    return aggregate_revenue(normalized)
