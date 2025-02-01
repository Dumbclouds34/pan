import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.randint(70,150, 15)
#vectorize timestamp conversion using pandas
timestamps = pd.to_datetime(data, unit='D',origin='unix')

#color list for each bar, excluding red
colors = ['green','pink','red','blue','yellow']
#set up the plot 
ax = plt.subplot()

#create the histogram with specified color for each bin
n, bins, patches = ax.hist(timestamps, bins=5, edgecolor='red', linewidth=1)

#apply custom colors to each bar through iteration

for i, patch in enumerate(patches):
    patch.set_facecolor(colors[i%len(colors)])

ax.set_title('My Histogram\nCheck it out')

#axis labels
ax.set_xlabel('value range')
ax.set_ylabel('frequency')

plt.show()