#!pip install numpy

## In this part, we will go over the basic array object in numpy
## We briefly came across this object when we discussed lists in python


import numpy as np
a = np.array([1, 2, 3])
#print(a)

# What we need to keep in mind is that object in a numpy array need to be of the same type

# For example, if we try to create an array and there is an element that is a string, all elements of the array are "forced" to be made into the <U21 (Unicode strings with less than 21 characters) type
b = np.array([1, 2, 'a'])
#print(b)

# We can also create multidimensional lists
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(c)
# We often refer to multidimensional arrays as matrices