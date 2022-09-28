import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('rainfall.csv')
df.info()
fig=plt.figure()
group_df=df.groupby(['STATE_UT_NAME']).count()[['DISTRICT']]
group_df.reset_index(inplace=True)
print(group_df)
ax=fig.add_subplot(111)
ax.set_title('bar chart')
ax.set_xlabel('states')
ax.set_ylabel('dist')
ax.bar(group_df['STATE_UT_NAME'],group_df['DISTRICT'])
fig.show()
