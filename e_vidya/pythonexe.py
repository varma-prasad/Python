import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#reading data
df=pd.read_csv('rainfall.csv')
print(df)
df.info()
df.dropna(inplace= True)
df.info()
#finding district having maximum rainfall
highraindist=df.loc[df['ANNUAL']==df['ANNUAL'].max()]
print(highraindist['DISTRICT'].values)

# top 5 states with highest annual rainfall
df_sort=df.sort_values(by='ANNUAL',ascending=False).head()
print(df_sort['DISTRICT'].values)

#Drop the columns 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'
df.drop(columns=['Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'], inplace =True)
df.info()

#Display the state-wise mean rainfall for all the months using a pivot table
print(pd.pivot_table(df,index='STATE_UT_NAME',aggfunc=np.mean))

#countof districts in each state
print(df.groupby('STATE_UT_NAME').count()[['DISTRICT']])

#For each state, display the district that gets the highest rainfall in May.Also display the recorded rainfall

print(df.groupby('STATE_UT_NAME').max()[['MAY']])
