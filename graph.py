import matplotlib.pyplot as plt
import numpy as np

#35,73,90,65,23,86,43,81,34,58

amount = 10
data = 35,73,90,65,23,86,43,81,34,58

list = np.random.randint(0,data,amount)
x = np.arange (0,amount,1)
n = len(list)

for i in range(n):
    for j in range(0,n-i-1):
        plt.bar(x,list)
        plt.pause(0.3)
        plt.clf()
        if list[j]> list[j+1]:
          list[j],list[j+1] = list[j+1],list[j]
plt.show()
