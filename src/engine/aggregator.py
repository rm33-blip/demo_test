def aggregate_revenue(rows: list) -> dict:
    """
    Aggregate revenue while treating None as missing.

    Returns:
      {
        "total_revenue": float,
        "valid_rows": int
      }
    """
    total = 0.0
    valid_count = 0

    for row in rows:
        revenue = row.get("revenue")
        if revenue is None:
            continue
        total += float(revenue)
        valid_count += 1

    return {"total_revenue": total, "valid_rows": valid_count}
