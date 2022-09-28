import numpy as ny
import pandas as pd
df=pd.read_csv("test.csv")
print(df)
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.info())
print(df['Period'])
print(df[['Subject']])
print(df[['Subject','STATUS','UNITS']])
