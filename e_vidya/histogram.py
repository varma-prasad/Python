import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('rainfall.csv')
df.info()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('Histogram')
ax.set_xlabel('ANNUAL')
ax.set_ylabel('RAINFALL')
ax.hist(df['ANNUAL'],bins=200)
fig.show()
