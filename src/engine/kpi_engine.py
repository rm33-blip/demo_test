def calculate_arpu(revenue: float, active_users: int):
    active_users = int(active_users)
    if active_users == 0:
        return None
    return float(revenue) / active_users


def calculate_churn_rate(lost_users: int, total_users: int):
    total_users = int(total_users)
    if total_users == 0:
        return None
    return float(lost_users) / total_users
