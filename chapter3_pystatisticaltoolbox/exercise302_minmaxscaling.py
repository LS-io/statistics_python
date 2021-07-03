## In this exercise we will write a function to apply the process of Min-Max scaling to a numerical attribute in our data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
## remoce the full filepath before commiting
#print(df.head())

#now we wil write our function to apply Min-Max scaling
def min_max_scale(data, a, b):
    data_max = np.max(data)
    data_min = np.min(data)

    return (a + (b - a) * ((data - data_min) / (data_max - data_min)))

## As we will consider the data in Column 1 first, let's plot a histogram to see the distribution of our attribute
# plt.hist(df['Column 1'], bins = 20)
# plt.show()

## Using the same plt.hist() function, we will visualise the the values after we apply our Min-Max funtion on it
# plt.hist(min_max_scale(df['Column 1'], -3, 3), bins = 20)
# plt.show()

## We could use the same process for the data in other columns as well, and we would see that the result is the same, we have scalled the data to the new range, without changing the shape of its distribution