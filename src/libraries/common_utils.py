import pandas as pd

def aggregate_rows(df):
    return pd.DataFrame({"total_sum_rows": df.sum(axis=1)})

