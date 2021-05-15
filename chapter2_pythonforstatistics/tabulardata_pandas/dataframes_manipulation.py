## Based on the MANIPULATING DATAFRAMES section in the book
## Here, we will focus on the how to use certain methods to manipulate the data within our DataFrame objects

import pandas as pd
import numpy as np

## For fun, let's try to store the methods from Figure 2.2 in the book inside a DataFrame and print them as a cheatsheet
methods = {
    'Method':[
        'rename(self[, axis, ...])',
        'fillna(self[, method, ...])',
        'replace(self, to_replace=None, value=None)',
        'drop(self[, labels, axis, ...])',
        "pd.concat(objs, axis=0, join='outer', ...)",
        'sort_values(self, by[, axis, ascending, ...])',
        'pd.read_csv()',
        'to_csv()'
        ],
    'Effect': [
        'Changes the albels of the rows or columns',
        'Replaces empty cells(that contain NA/NaN values) using a specific method',
        'replaces cells that contain the value passed to to_replace by the value passed to value',
        'Drops specific rows or columns from the data table',
        'Concatenates pandas objects along the specified axis',
        'Sorts by values along the specified axis',
        'Reads a CSV text file and returns the corresponding DataFrame object',
        'Writes a DataFrame object to file as a CSV text file'
    ]}
methods = pd.DataFrame(data = methods)
#print(methods)


## Now we can start with exercise
## Exercise 2.02: DATA TABLE MANIPULATION
## We have created a copy of the dataset.csv file (included in this repository)
## In the beginning of this script, we have imported pandas and numpy, otherwise we would do it here
#import pandas as pd
#import numpy as np

## We read the .csv file by using the pd.read_csv() methond
df = pd.read_csv('B:/Coding/GitHub/statistics_python/statistics_python/chapter2_pythonforstatistics/tabulardata_pandas/dataset.csv', index_col = 'id')
#print(df)
## We can notice that we have two instances of NaN as an elements in our DataFrame
## Normally, NaN is the defaul value for empty cells
## Lastly, NaN are registered as floats in Python, hence all of our elements in the y and z column were converted into float type accordingly

## Next, we can use the rename() method to change the name of our columns
df = df.rename(columns = {'x': 'col_x', 'y': 'col_y', 'z': 'col_z'})
#print(df)

## Next, we will use the fillna() funciton to replace the NaN values with zeros.
df = df.fillna(0)
## Then, we convert all the values into integers (previously they were float due to NaNs)
df = df.astype(int)
## Let's check what the DataFrame looks like now
#print(df)

## We will now remove the second, fourth and fifth rows from the dataset with the drop() method
df = df.drop([1, 3, 4], axis = 0)
#print(df)
## To drop columns instead of rows, we specify axis = 1

## Now, let's create a DataFrame the size of 2 x 3 with all zero elements
zero_df = pd.DataFrame(np.zeros((2, 3)), columns = ['col_x', 'col_y', 'col_z'])
#print(zero_df)

## Next, we can concatenate the two tables together
## In the concatenate() method, we specify axis = 0, so that the tables are joind verticall instead of horizontally
df = pd.concat([df, zero_df], axis = 0)
#print(df)

## We need to sort our current table in increasing order by the first column (not index column)
df = df.sort_values('col_x', axis = 0)
#print(df)

## Finally, we will convert our table into the integer type and write it to a .csv file (which we will name output)
## We specify index = False, in order for the index column not to be included in the output
df = df.astype(int)
df.to_csv('output.csv', index = False)