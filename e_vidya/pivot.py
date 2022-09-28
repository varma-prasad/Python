# merge vs concat
import numpy as np
import pandas as pd
df=pd.read_csv('test.csv')
print(df)
print(df.info())
print(df.groupby(['Data_value','UNITS']))
pivot=pd.pivot_table(df,index='Period')
print(pivot)
