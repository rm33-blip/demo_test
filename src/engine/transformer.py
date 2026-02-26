from src.config.schema import EXPECTED_SCHEMA_V1

class SchemaValidationError(Exception):
    pass

def normalize_row(row: dict):
    unexpected_columns = set(row.keys()) - set(EXPECTED_SCHEMA_V1.keys())
    if unexpected_columns:
        raise SchemaValidationError(
            f"Unexpected columns detected: {unexpected_columns}"
        )

    normalized = {}
    for key in EXPECTED_SCHEMA_V1:
        normalized[key] = row.get(key)

    return normalized
