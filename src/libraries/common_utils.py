import pandas as pd

def aggregate_rows(df):
    return pd.DataFrame({"total_sum": df.sum(axis=1)})


