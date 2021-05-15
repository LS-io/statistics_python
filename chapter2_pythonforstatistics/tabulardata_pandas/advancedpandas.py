## The ADVANCED PANDAS FUNCTIONALITIES focuses on other options for accessing and changing the values inside a pandas DataFrame object
## First method we will look at is the apply() method
import pandas as pd
## First we need to initialise our DataFrame object
df = pd.DataFrame({'x': [1, 2, -1], 'y': [-3, 6, 5], 'z': [1, 3, 2]})
#print(df)

## We want to create another column whose entries are the entries in the x_squared column
df['x_squared'] = df['x'].apply(lambda x: x ** 2)
#print(df)
## The term lambda x: x ** 2 is a quick way to declare a function without a name
## With what we know from NumPy, the following code will have the same output
#df['x_squared'] = df['x'] ** 2
## Other functions might not be as easily vectorised however


## E.g. let's create another column, where each element is a string that says if the value in the x column is even or odd
def parity_str(element):
    if element % 2 == 0:
        return 'even'
    
    return 'odd'

df['x_parity'] = df['x'].apply(parity_str)
#print(df)


## Another commonly used functionality that is slightly more advanced is the pandas.get_dummies() function
## It allows us to implement the so-called one-hot encoding, which is used on a categorical attribute (or column) in a dataset
## One-hot encoding works by generating a new column/attribute for each unique vale and populates the cells in the new column with Boolean data
## For example, the x_parity column we created above holds categorical attributes since the values belong to a specific set of categories (odd and even)
## When we call the get_dummies() function on the x_parity columns, we produce a new object with the following values
dummies = pd.get_dummies(df['x_parity'])
#print(dummies)

## We can by looking at the original df, we can see by comparison that this object tells us where (in which rows) each of the categorical values are located
# print(df)
# print('-' * 50)
# print(dummies)

## With one-hot encoding we can convert any categorical attribute into a new set of binary attributes, making the dataset readable for statistical and machine learning models
## HOWEVER, this method add the same number of additional columns as many categorical attributes we have, so it is a big increase of dimensionality, which affects the computational (and hence time) complexity


## The next method we will look at is the value_counts() method.
## This method is called on the column of a DataFrame object, and returns a list of unique values in that column and their respective counts. The method is thus only applicable to categorical and discrete data
## E.g., still considering the x_parity attributes, we can inspect the effect of the value_counts()
print(df['x_parity'].value_counts())
## We can observe that we get two rows (two entries) whose values are odd and even, and the amounts for each entry


## The last method we will look at is the groupby operation, which we will use in the exercise 203 file