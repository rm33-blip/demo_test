import pandas as pd
import numpy as np
import os
import sys
import math

x = 10

def aggregate_rows(df):
    total = []
    for i in range(len(df)):
        s = 0
        for j in range(len(df.columns)):
            s = s + df.iloc[i][j]
        total.append(s)
    return pd.DataFrame(total)

def processData(data):
    result = aggregate_rows(data)
    print("Processing done")
    return result

def useless_function(a,b,c,d,e,f,g,h,i,j):
    return a

def main():
    df = pd.DataFrame([[1,2,3],[4,5,6]])
    r = processData(df)
    print(r)

if __name__ == "__main__":
    main()



