## We start by importing the pandas package
import pandas as pd
import numpy as np

## Pandas utilises a DataFrame object.
## We can manually create one by passing in a Python dictionary, where each key is the name of the column, and the value should be the data stored for that column; in the form of a list or a NumPy array.
my_dict = {'col1': [1, 2], 'col2': np.array([3, 4]), 'col3': [5, 6]}
df = pd.DataFrame(my_dict)
#print(df)

# We can also initialise a dataframe directly from a 2D NumPy array
my_array = np.array([[1, 3, 5], [2, 4, 6]])
df = pd.DataFrame(my_array, columns = ['col1', 'col2', 'col3'])
#print(df)


## Accessing rows and columns
## Once we have a table of data in a DataFrame object, we can perform several options in order to access it and manipulate the data in it.
## When we want to access a group of rows or columns, we can take a look at the loc method, which takes labels of the rows/columns and return the values
#print(df.loc[0])

#print(df.loc[[0, 1]])

## If we want to access the data in our table column-wise
#print(df.loc[0, ['col2', 'col3']])


## If we want to access the whole column, we can perform two commands
#print(df.loc[:, 'col3'])
## Or more simplified
#print(df['col3'])

## We can also iterate on the DataFrame object
# def iterate():
#     for item in df['col3']:
#         print(item)

# iterate()

## Or simply
# for item in df['col3']:
#     print(item)


## We can also change the values in our DataFrame object
df.loc[0] = [3, 6, 9] # change the first row
print('Change the first row')
print(df)
print('-' * 50)
df['col2'] = [0, 0] # Change the second column
print('Change the second column')
print(df)


## Similarly, we can declare new rows and columns
print('Original DataFrame:')
print(df)
print('-' * 50)
df['col40'] = [10, 10]
print('Declare new column:')
print(df)
print('-' * 50)
df.loc[3] = [1, 2, 3, 4]
print('Declare new row:')
print(df)


## Finally, we can use the Boolean values to access the values in the DataFrame
## E.g. for the elements in the second row and second and fourth column
print('-' * 100)
print(df.loc[[False, True, False], [False, True, False, True]])

## Similarly, we can use this approach to replace only the values of elements that meet our criteria
print('-' * 50)
print(df.loc[:, df.loc[0] > 5])