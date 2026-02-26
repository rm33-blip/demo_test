class ValidationError(Exception):
    pass


def apply_validation_rules(row: dict, rules: list):
    """
    Apply validation rules to a single row.

    Supported rules:
      - greater_than: row[field] must be > value
    """
    for rule in rules or []:
        field = rule.get("field")
        op = rule.get("rule")
        value = rule.get("value")

        if field is None or op is None:
            continue

        if op == "greater_than":
            current = row.get(field)
            # Treat None as invalid for this rule
            if current is None or float(current) <= float(value):
                raise ValidationError(f"{field} must be > {value}")
        else:
            raise ValidationError(f"Unknown validation rule: {op}")
