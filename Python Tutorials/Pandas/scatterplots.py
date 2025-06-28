import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
colors=np.array([10,20,30,40,50])

plt.scatter(x,y, c=colors, cmap='viridus')
plt.show()
