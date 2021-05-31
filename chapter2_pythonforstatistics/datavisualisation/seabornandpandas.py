## Visualisation with Seaborn and Pandas

## Similarly to how we explored visualisation with the matplotlib library, we can also use other python packages for visualising our data, seaborn being one of them.

## Let's explore how we can utilise seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.normal(0, 1, 1000)
y = np.random.normal(5, 2, 1000)

df = pd.DataFrame({'Column 1': x, 'Column 2': y})
#print(df.head)

## Since we want to create two histograms and view them together, we can use the jointplot() function
#sns.jointplot(x = 'Column 1', y = 'Column 2', data = df)
#plt.show()

####################################################################################################
## Anothe example, where we consider the student dataset from exercise 2.03
student_df = pd.DataFrame({
    'name':
        ['Alice', 'Bob', 'Carol', 'Dan', 'Eli', 'Fran', 'George', 'Howl', 'Ivan', 'Jack', 'Kate'],
    'gender':
        ['female', 'male', 'female', 'male', 'male', 'female', 'male', 'male', 'male', 'male', 'female'],
    'class':
        ['JR', 'SO', 'SO', 'SO', 'JR', 'SR', 'FY', 'SO', 'SR', 'JR', 'FY'],
    'gpa':
        [90, 93, 97, 89, 95, 92, 90, 87, 95, 100, 95],
    'num_classes':
        [4, 3, 4, 4, 3, 2, 2, 3, 3, 4, 2]
})
## Again, we want to consider the average GPA of the students, grouped by class
#sns.catplot(x = 'class', y = 'gpa', hue = 'gender', kind = 'bar', data = student_df)
#plt.show()

####################################################################################################
## Additionally, the pandas library itself also offers unique APIs that directly interact with Matplotlib
student_df['gpa'].plot.hist()
plt.show()
## We can also generate a piechart from the class count
student_df['class'].value_counts().plot.pie()
plt.show()