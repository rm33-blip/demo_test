SUPPORTED_SCHEMA_VERSIONS = {"v1"}


class SchemaVersionError(Exception):
    pass


def validate_schema_version(schema_version: str):
    if schema_version not in SUPPORTED_SCHEMA_VERSIONS:
        raise SchemaVersionError(
            f"Unsupported schema_version: {schema_version}. "
            f"Supported: {sorted(SUPPORTED_SCHEMA_VERSIONS)}"
        )
