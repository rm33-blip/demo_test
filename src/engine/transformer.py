from src.config.schema import EXPECTED_SCHEMA_V1


class SchemaValidationError(Exception):
    """Raised when input row schema does not match expected schema."""
    pass


def normalize_row(row: dict) -> dict:
    """
    Normalize incoming row to EXPECTED_SCHEMA_V1 keys.

    Enforces schema drift detection:
      - If row contains unexpected columns, raise SchemaValidationError.
    """
    unexpected = set(row.keys()) - set(EXPECTED_SCHEMA_V1.keys())
    if unexpected:
        raise SchemaValidationError(f"Unexpected columns detected: {sorted(unexpected)}")

    normalized = {}
    for key in EXPECTED_SCHEMA_V1:
        normalized[key] = row.get(key)
    return normalized
