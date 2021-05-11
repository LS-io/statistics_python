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


## We can also use methods np.zeros() and np.ones() to create a matrix full of zeros or ones
zero_array = np.zeros((2, 2)) # This creates a 2 by 2 matrix
#print(zero_array)

ones_array = np.ones((2, 3, 5), dtype = int) # Creates a 3D integer matrix
#print(ones_array)


## Similarly to zeros and ones, we can generate a matrix filled with random numbers
random_array = np.random.rand(2, 3, 4)
#print(random_array)
# We see that this generate a matric with random float values between 0 (inclusive) and 1 (exclusive)
# If we want to generate a matrix of random integers, we can use the np.random.randint() method
randomint_array = np.random.randint(0, 10, size = (2, 3, 4))
#print(randomint_array)

########################################################################################################
## Similar method I like to use, that generate a matrix with random values from a specific distribution:
## * np.random.normal --> returns random values from a normal (Gauss) distribution
## * np.random.pareto --> returns random values from a pareto distribution
## * np.random.power --> returns random values from a power distribution
########################################################################################################


## Keep in mind, that when calling multidimensional arrays, we simply need to separate the individual indices with commas
## Although calling with separated square brackets also works


## Slicing a NumPy array can be done very similarly - by using commas
## We will create a new, or rather "overwrite" the existing, array in variable a
a = np.random.rand(2, 3, 4) # We get a random 2-by-3-by-4 matrix
#print(a)
#print('-' * 50)
## We slice with the specified indices
#print('''The sliced version using a[1, 0:2, 1:] command:
#''')
#print(a[1, 0:2, 1:])


## Another important syntax is the np.reshape() method, which allows us to change the shape of the array.
## Keep in mind, that we need to specify a shape that still encompasses the same number of values
# print(a)
# print('''
# The shape of array a:
# ''', a.shape)
# print('''

# Let's see what it looks like, when we use the np.reshape(a, (3, 2, 4)) call:
# ''', np.reshape(a, (3, 2, 4)))


## Finally, let's take a look how we can transpose a matrix
## Transposing a matrix is flipping the elements along the matrix's diagonal
## In NumPy, this can be done quite simply by calling [array].T
print(a.T)