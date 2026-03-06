class ValidationError(Exception):
    pass


def apply_validation_rules(row: dict, rules: list):
    """
    Apply validation rules to a single row.

    Supported rules:
      - gt: row[field] must be > value
    """
    for rule in rules or []:
        field = rule.get("field")
        op = rule.get("rule")
        value = rule.get("value")

        if field is None or op is None:
            continue

        if op == "gt":
            current = row.get(field)
            if current is None or float(current) <= float(value):
                raise ValidationError(f"{field} must be > {value}")
        else:
            raise ValidationError(f"Unknown validation rule: {op}")
