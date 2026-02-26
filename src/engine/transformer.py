from src.config.schema import EXPECTED_SCHEMA_V1


class SchemaValidationError(Exception):
    """Raised when input row schema does not match expected schema."""
    pass


def normalize_row(row: dict) -> dict:
    """
    Partial schema validation fix:
      - Detect missing columns (but does NOT detect unexpected columns).
    """
    missing = set(EXPECTED_SCHEMA_V1.keys()) - set(row.keys())
    if missing:
        raise SchemaValidationError(f"Missing columns detected: {sorted(missing)}")

    normalized = {}
    for key in EXPECTED_SCHEMA_V1:
        normalized[key] = row.get(key)
    return normalized
