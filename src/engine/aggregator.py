def aggregate_revenue(rows: list):
    total = 0
    for row in rows:
        total += row.get("revenue", 0)
    return total
