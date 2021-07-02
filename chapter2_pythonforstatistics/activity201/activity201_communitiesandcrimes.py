## This activity will focus on some basic data processing and analysing techniques on a dataset, available online, called Communities and Crime.
## We wish to leverage our knowledge gained thus far.

## The packages we will be using
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
## We start by downloading the dataset adn importing it with
data_url = 'CommViolPredUnnormalizedData.txt'
## Remove the full url before commiting
raw_data = pd.read_csv(data_url, sep = ',')

## (2) We want to display the firt five rows of the dataset
#print(raw_data.head(5))

## (3) Now we want to loop through the columns in the dataset and print the out line by line.
## At the end, we want to print out the total number of columns
column_count = 0
for column in raw_data:
    #print(column)
    column_count += 1
#print(column_count)

## (4) Next, we want to to replace the missing values with np.nan
df = raw_data
df = df.replace('?', np.nan)
#print(data)

## (5) Now let's display the list of missing values per column
#print(df.isnull().sum())

## (6) we want to know the number of missing values in the NumStreet and PolicPerPop columns
#print(df.isnull().sum()['NumStreet'])
#print(df.isnull().sum()['PolicPerPop'])

## (7) Let's disply the counts of different values in the state columnd
states = df['state'].value_counts()
#states.plot.bar()
#plt.show()

## (8) We can notice that the labels on the x-axis are overlapping, so let's change the plot size
# f, ax = plt.subplots(figsize = (15, 10))
# states.plot.bar()
# plt.show()

## (9) Now we will display the same values in a pie chart. Adjust the size as necessary
#states.plot.pie()
#plt.show()

## (10) Next, we will display the distribution of population sizes in a histogram
f, ax = plt.subplots(figsize = (12, 8))
# df['population'].hist(bins = 200)
# plt.show()

## (11) Finally, we want to equivalently visualise the distribution of household sizes in the dataset
df['householdsize'].hist(bins = 250)
plt.show()