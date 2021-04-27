## String is a senquence of characters, that are typically used to represent textual information, e.g. a message.
## In python, a string is denoted as any given data inside single- or double-quotation marks
# In the example below, variables a and b hold the same information
a = 'Hello, world!'
b = "Hello, world!"

## Strings are roughly treated as sequences in python, so common sequence-related operations can be applied to this data structure.
## e.g. we can concatenate two or more strings together to create a longer string
a = 'Hello, '
b = 'world!'
print(a + b)

for char in a:
    print(char)

print(b[2])

print(a[1:4])