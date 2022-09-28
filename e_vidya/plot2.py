import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(1,16)
y=x**2
z=(y/2)+40

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,color='g',label='line1')
ax.plot(x,z,color='r',label='line2')
ax.set_title('The title of plot',fontsize=15)
ax.set_xlabel('label of x axis',fontsize=15)
ax.set_ylabel('label of y axis',fontsize=15)
ax.legend()
plt.show()
