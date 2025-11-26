import numpy as np # import numpy
import matplotlib.pyplot as plt

# x = np.array(range(1,11)) # list from 1 to 10 using numpy array

# y = x ** 2 - 4 # squre x and substract 4 for each element

# print(y) # print calculated elements

# print(np.zeros(10)) # create list of 10 zeros
# print(np.ones(10)) # create list of 10 ones

# print(np.arange(1,10,1)) 

# xs = np.array([1,5,9]) # define two arrays(vectors)
# a = np.arange(1,5)[:3] # slice array to have same shape as xs 
# print(xs + a) # add two vectors
# print(xs <= a) # check element wise

# plt.plot([1,2,3], [6,7,8]) # create x and y values
# plt.show() # show plot

# xv = np.arange(-3, 3, 0.1)
# yv = xv ** 3 - xv ** 2 + 6

# plt.scatter(xv, yv)
# plt.plot(xv, yv)
# plt.show()

xs = np.array([ # create matrix
    [1, 2, 3, 4, 5], 
    [1, 2, 3, 4, 5], 
    [4, 5, 6, 7, 8]])

# print(xs.shape) # print shape of xs
# print(xs[0]) # access first row of the matrix
# print(xs[:,0]) # access first column
# print(xs[2,4]) # access element in thrid row and fifth column 

# xs[0,0] = 10 # change first element to 10
# xs[:,3] = 15 # change fourth column to 15
# xs[:,2] = np.array([101,102,103]) # change third column to array elements
# print(xs)

# print(xs.reshape(-1)) # reshape matrix to one row
# print(xs.reshape(5, 3)) # reshape with 5 rows and 3 columns
# print(xs.reshape(5, -1)) # reshape with 5 rows and 3 columns, automatically detect number of columns
# print(xs.reshape(-1,1)) # reshape to multidimensional array conataining each element as array

print(xs.min())
print(xs.max())
print(xs.mean())

print(xs.min(axis=0)) # minimum of columns
print(xs.min(axis=1)) # minimun of rows
# axis works for max, mean and so on as well

print(xs.argmin()) # get position of minimum
print(xs.argmax()) # get position of maximum