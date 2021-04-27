## A tuple is declared by parentheses (instead of square brackets like a list).
## While tuples can still consist of elements of various data types, they are, in contrast to lists, immutable. This means they can not be mutated, changed, but remain as they were when initialised
a = (1, 2)
a[0] = 3 #Gives an error statement
a.append(2) #Also doesn't work

#They are useful for storing definite values that we don't want to change afterwards