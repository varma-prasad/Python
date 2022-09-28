import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating sample data for plotting
x = np.arange(1,16)    #1 … 15
y = x**2    #square of x values
z = (y/2)+40    #arithmetic operation applied to y values
#creating an empty canvas/figure
fig = plt.figure(figsize=(8,5))
#setting axes as [left, bottom, width, height]
ax1 = fig.add_axes([0.05,0.05,1.05,1.05])
ax2 = fig.add_axes([0.10,0.42,0.45,0.45])
#plotting the lines
ax1.plot(x,y,color="g", label='line1' )
ax1.set_title('Title for Plot 1',fontsize=15)    #setting title
ax1.set_xlabel('Plot 1 - X axis',fontsize=15)    # setting X label
ax1.set_ylabel('Plot 1 - Y axis',fontsize=15)    # setting Y _label
ax2.plot(x,z,color="r", label='line2')
ax2.set_title('Title for Plot 2',fontsize=15)    #setting title
ax2.set_xlabel('Plot 2 - X axis',fontsize=15)    # setting X label
ax2.set_ylabel('Plot 2 - Y axis',fontsize=15)    # setting Y _label
ax1.legend()    #adding legend
ax2.legend()
plt.show()
