import pandas as pd

def aggregate_rows(df: pd.DataFrame) -> pd.DataFrame:
    # Correct implementation
    return pd.DataFrame({"total_sum": df.sum(axis=1)})
