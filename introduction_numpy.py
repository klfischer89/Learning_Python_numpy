import numpy as np # import numpy
import matplotlib.pyplot as plt

x = np.array(range(1,11)) # list from 1 to 10 using numpy array

y = x ** 2 - 4 # squre x and substract 4 for each element

# print(y) # print calculated elements

# print(np.zeros(10)) # create list of 10 zeros
# print(np.ones(10)) # create list of 10 ones

# print(np.arange(1,10,1)) 

xs = np.array([1,5,9]) # define two arrays(vectors)
a = np.arange(1,5)[:3] # slice array to have same shape as xs 
# print(xs + a) # add two vectors
# print(xs <= a) # check element wise

# plt.plot([1,2,3], [6,7,8]) # create x and y values
# plt.show() # show plot

xv = np.arange(-3, 3, 0.1)
yv = xv ** 3 - xv ** 2 + 6

# plt.plot(xv, yv)
# plt.show()

