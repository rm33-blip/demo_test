def validate_row_types(row: dict, schema: dict):
    for field, expected_type in schema.items():
        if field in row and not isinstance(row[field], expected_type):
            raise TypeError(f"Invalid type for {field}")
