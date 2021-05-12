## In computer science, the term vectorisation denotes a process of applying a mathematical operation to an array, element by element.
## E.G. an add operation where every element in an array is added to the same term is a vectorised operation; same goes for vectorised multiplication, where all elements in an array are multiplied by the same term.
## In general, vectorisation is successful when all the elements are put through the same function

## In NumPy, vectorisation can be optimised to be more efficient by a for loop (for example). The requirement is, that all elements are of the same type, which is a requirement for a NumPy array anyway.


## Timing vectorised operations in NumPy
import numpy as np
from timeit import Timer

my_list = list(range(10 ** 6))
my_array = np.array(my_list)

# We define a funciton for_add(), which will return us a list where elements of the input (original) list have 1 added to them.
def for_add():
    return [item + 1 for item in my_list]

# We write a separate function, which returns the NumPy version of the same data, which we will call vec_add
def vec_add():
    return my_array + 1

## We will now initialise two Timer objects while passing each of our two functions. These objects contain the interface that we will use to keep track of the speed of the functions
## By calling the repeat() function on each of the objects with arguments 10 and 10, we are in essence repeating the timing experiment 100-times. This returns a list of all the times that were required for the operation to run.
## By calling to print the minimum of the list, we get the fastest time of execution.
#print('For-loop addition:')
#print(min(Timer(for_add).repeat(10, 10)))

# print('Vectorised addition:')
# print(min(Timer(vec_add).repeat(10, 10)))
# We can see that the vectorized addition in case of NumPy is many-fold quicker


## We will now implement the same comparison of speed where we multiply the numbers by 2.
def for_mul():
    return [item * 2 for item in my_list]

def vec_mul():
    return my_array * 2

# print('For-loop multiplication')
# print(min(Timer(for_mul).repeat(10, 10)))

# print('Vectorised multiplication')
# print(min(Timer(vec_mul).repeat(10, 10)))
# Again, we see that the vectorised approach is much quicker


## Now we will shall implement the same comparison, finally comparing the computation of a square root of numbers
## For this, we need to import the math module to implement with the Python list
import math

def for_sqrt():
    return [math.sqrt(item) for item in my_list]

def vec_sqrt():
    return np.sqrt(my_array)

# print('For-loop square root:')
# print(min(Timer(for_sqrt).repeat(10, 10)))
# print('Vectorised square root:')
# print(min(Timer(vec_sqrt).repeat(10, 10)))
# While your output might be different, we see that the vectorised operation is considerably quicker