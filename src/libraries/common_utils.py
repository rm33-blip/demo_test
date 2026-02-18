import pandas as pd

def aggregate_rows(df):
    return pd.DataFrame({"sum_total": df.sum(axis=1)})


