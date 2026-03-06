from src.config.schema import EXPECTED_SCHEMA_V1


class SchemaValidationError(Exception):
    """Raised when input row schema does not match expected schema."""
    pass


def normalize_row(row: dict, fail_on_unexpected_columns: bool = False) -> dict:
    """
    Schema validation:
      - Always detect missing columns
      - Optionally detect unexpected columns
    """
    missing = set(EXPECTED_SCHEMA_V1.keys()) - set(row.keys())
    if missing:
        raise SchemaValidationError(f"Missing columns detected: {sorted(missing)}")

    if fail_on_unexpected_columns:
        unexpected = set(row.keys()) - set(EXPECTED_SCHEMA_V1.keys())
        if unexpected:
            raise SchemaValidationError(f"Unexpected columns detected: {sorted(unexpected)}")

    normalized = {}
    for key in EXPECTED_SCHEMA_V1:
        normalized[key] = row.get(key)
    return normalized
