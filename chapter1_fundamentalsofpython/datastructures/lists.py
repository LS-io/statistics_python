## Lists are the most used data structure in python. Equivalent in Java or C/C++ is an array
## In a python list, elements do not need to be of the same data structure
a = [1, 'a', (2, 3), 2]
#print(a[2]) ## Output: (2, 3)
#print(a[1: 3]) ##Output: ['a', (2, 3)]

## We can add new elements to a list in two ways (in python)
# First solution is to use the .append() method
a = [1, 'a', (2, 3)]
a.append(3)
#print(a)
# Similarly, we can use the .pop() method to remove an element from the list at the selected index

# The second solution is to concatenate two lists together, as demonstrated below
b = [2, 5, 'b']
#print(a + b) ##Output: [1, 'a', (2, 3), 3, 2, 5, 'b']



## Another interesting, and significant, operation is list comprehension
## List comprehension is an operation where we efficiently initialize lists using a for loop placed inside a square bracket. Typical use is when we want to apply an operation to an existing list to create a new one
a = [1, 4, 2, 9, 10, 3]
# We want to create a new list, called b, which consists of elements from a, multiplied by 2
b = [2 * element for element in a]
#print(b)

# Furthermore, let's create a list c, that applies the same rule, but only if the element from a is an odd number.
c = [2* element for element in a if element % 2 == 1]
#print(c)