import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('rainfall.csv')
df.info()
fig=plt.figure()
ax=fig.add_subplot(111)
line_df=df.groupby('STATE_UT_NAME')
line_df=line_df.mean()
ax.set_title('Annual vs jan vs feb')
ax.set_xlabel('State')
ax.set_ylabel('Value')
ax.plot(line_df['ANNUAL'],label='Annual',linestyle='-')
ax.plot(line_df['JAN'],label='jan',linestyle='--')
ax.plot(line_df['FEB'],label='feb')
ax.legend()
fig.show()
