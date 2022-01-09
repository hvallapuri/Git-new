import pandas as pd
import os

def sparktest():
    df = pd.read_csv("data/data.csv")
    print(df.columns)

sparktest()