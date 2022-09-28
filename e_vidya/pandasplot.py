# merge vs concat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('test.csv')
print(df)
print(df.info())
df.plot(x = 'Period', y = 'Data_value', marker = 'o', kind = 'scatter')
df.groupby('Period').mean()[['Data_value']].plot(kind='bar')
plt.show()
