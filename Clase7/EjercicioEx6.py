from matplotlib import pyplot as plt
import numpy as np

a = np.array([40,40,40,40,40,40,40,10,10,10,45]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histograma") 
plt.show()