from src.config.schema import EXPECTED_SCHEMA_V1

def normalize_row(row: dict):
    normalized = {}
    for key in EXPECTED_SCHEMA_V1:
        normalized[key] = row.get(key)
    return normalized
