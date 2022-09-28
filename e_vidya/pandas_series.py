import numpy as np
import pandas as pd
series = pd.Series(data = [78, 92, 36, 64, 89])  
print(series)
print(series.values)
print(series.index)
print(series[2])
print(series[1:3])

#by default series creates integer index

car=['swift','jazz','civic','altis','gallardo']
prize=[70000,80000,160000,180000,3000000]
data=pd.Series(data = prize,index = car)
print(data)
print(data['swift'])
print(data['civic':'altis'])
