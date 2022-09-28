import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(0.0,5.0,0.1)
y=np.cos(2*np.pi*x)*np.exp(-x)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('Figure Title')
ax.set_xlabel('Abscisa')
ax.set_ylabel('Ordinate')
ax.plot(x,y)
fig.show()
