from src.engine.transformer import normalize_row
from src.engine.aggregator import aggregate_revenue

def process(rows: list):
    normalized = [normalize_row(r) for r in rows]
    total = aggregate_revenue(normalized)
    return total
