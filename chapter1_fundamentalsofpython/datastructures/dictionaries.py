## Python dictionaries are the equivalent of hash maps in Java, where we can specify key-value pair relationships and perform lookups on a key to obtain its corresponding value.


# We declare a dictionary in python by listing key-value pairs in the form of key: value, separated by commas inside of curly brackets {}
score_dict = {'Alice': 90, 'Bob': 85, 'Carol': 86}
#print(score_dict)


# The value of a given key can be accessed by passing the key to the dictionary inside square brackets
#print(score_dict['Alice'])
#OUT: 90

#print(score_dict['Carol'])
#OUT: 86


# Changing the value of a key, or adding a new key, can be done using the same syntax
score_dict['Alice'] = 89
#print(score_dict)
score_dict['Chris'] = 85
#print(score_dict)


# Similar to list comprehension, we can use dictionary comprehension
square_dict = {i: i ** 2 for i in range (-1, 4)}
#print(square_dict)


# We can also delete a key-value pair from a dictionary, using the del keyword
del score_dict['Alice']
print(score_dict)