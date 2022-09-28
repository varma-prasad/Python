import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('rainfall.csv')
df.info()
fig=plt.figure(figsize=[6,6])
ax=fig.add_subplot(111)
ax.set_title('annual')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.boxplot(df['ANNUAL'])
fig.show()

new_list=[df['ANNUAL'],df['DEC']]
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('new')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.boxplot(new_list)
fig.show()
