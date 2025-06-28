import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
my_lables=['Apples','Bannana','cherry','Mango']
my_explode=[0.1,0,0,0]  #for separating the segment

plt.pie(y,labels=my_lables,startangle=90,explode=my_explode,shadow=True)
plt.legend(title='fruits')
plt.show()