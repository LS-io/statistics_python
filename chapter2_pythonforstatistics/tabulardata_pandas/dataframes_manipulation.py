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
