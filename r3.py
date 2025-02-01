import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as an

# set up/create the figure and axis
fig, ax = plt.subplots()

# generate initial random data
data = np.random.randint(70, 150, 15)

#create initial histogram plot on the axis (ax) using ax.hist
#pass the (data) as the input
ax.hist(data, bins=10, color= 'blue', rwidth=0.98 )

#labels and title, setting the x-axis limits to [70,150] using ax.set(xlim=...)
ax.set(xlim=[70,150], xlabel= 'Data Values', ylabel='Frequency', title= 'Real-Time Updating Histogram')
ax.legend()

#function to update the histogram for each frame
def update(frame):
    #simulate incoming new data by generating a new random value
    n_data = np.random.randint(70, 150, 15)
    #append new data to the existing data
    #using the (global) keyword to access the (data) variable  from the outer scope
    #append the new data(_data) to the existing data(data) using (np.append)
    global data
    data = np.append(data, n_data)
    # clear the histogram and replot with updating data 
    #clears axis to refresh plot
    ax.cla()
    ax.set(xlim=[70, 150], xlabel = 'Data values', ylabel ='Frequency', title= 'Real-Time Updating Histogram')

    #plots updated histogram
    ax.hist(data, bins=10, color= 'blue', rwidth=0.98)

    plt.xlabel('Data Values')
    plt.ylabel('Frequency')
    plt.title('Real-Time Updating Histogram')

    #creates an animation
    #create an animation using an.FuncAnimation(). 

Animation = an.FuncAnimation(fig=fig, func=update, frames=20, interval=1000 )
plt.show()