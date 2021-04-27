## A set is declared with curly brackets {}.
## In python, a set is a collection of unordered elements
a = {1, 2, 3}
a.add(4)
#print(a)

# An element, that already exists in the set, can not be added again.
a.add(3)
print(a)

# One of the most common operations is to join two sets using the union() and intersection() methods.
a = {1, 2, 3, 4}
b = {2, 5, 6}
print(a.union(b))
print(a.intersection(b))