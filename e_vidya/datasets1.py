import numpy as ny
import pandas as pd
df=pd.read_csv("test.csv")
print(df)
df_head=df.head()
print(df_head)
df_head.set_index('Period',inplace=True)
print(df_head)
print(df.info())
print(df.iloc[1:4,4:8])
print(df.loc[0:3,['Period','UNITS']])
