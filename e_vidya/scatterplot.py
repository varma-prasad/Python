import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('rainfall.csv')
df.info()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(df['ANNUAL'],df['JAN'])
ax.set_title('annual vs jan')
ax.set_xlabel('annual')
ax.set_ylabel('jan')
fig.show()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('annual vs jan')
ax.set_xlabel('annual')
ax.set_ylabel('jan')
state_list=df['STATE_UT_NAME'].unique()
print(state_list)
colors=plt.get_cmap(np.linspace(0,1,len(state_list)))
for state,colors in zip(state_list,colors):
    x=df[df['STATE_UT_NAME']==state]['ANNUAL']
    y=df[df['STATE_UT_NAME']==state]['JAN']
    plt.scatter(x,y,color=color,label=state)
plt.legend()
fig.show()
