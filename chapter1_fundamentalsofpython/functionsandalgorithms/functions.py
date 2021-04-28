## In python, a function is a specific object with which we can order and factor our programs
## The term algorithms typically refers to the general organisation of a sequence of logic to process its given input data

##In it's most abstract definition, a function as an object takes an input and produces an output
#def function_name(parameter1, parameter2, ...):
#    [...]
#    return [...]

#name = input('Your name: ')

def greet(name):
    print(f'Hello, {name}!')

#greet(name)


def get_first_even(my_list):
    for item in my_list:
        if item % 2 == 0:
            return item
    return False #should be the first even element
