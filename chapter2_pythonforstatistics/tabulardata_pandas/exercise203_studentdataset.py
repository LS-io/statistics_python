## In this exercise, we will look at the student dataset sample
## First, let's generate our dataset
import pandas as pd

students = pd.DataFrame({
    'name':
        ['Alice', 'Bob', 'Carol', 'Dan', 'Eli', 'Fran'],
    'gender':
        ['female', 'male', 'female', 'male', 'male', 'female'],
    'class':
        ['FY', 'SO', 'SR', 'SO', 'JR', 'SR'],
    'gpa':
        [90, 93, 97, 89, 95, 92],
    'num_classes':
        [4, 3, 4, 4, 3, 2]
    })

#print(students)

## Next we want to check whether the students are female or not
students['female_flag'] = students['gender'].apply(lambda x: x == 'female')
## Alternatively, we could also use
#students['female_flag'] = students['gender'] == 'female'
#print(students)

## As this new columns contains all the information included in the old gender column, we can remove it now
students = students.drop('gender', axis = 1)
#print(students)

## Now we can use the one-hot encoding approach to see how many different values we have for the class attributes in a way that "numerically readable"
dummies = pd.get_dummies(students['class'])
#print(dummies)

## Now we will see how the groupby() method can be used
## We will call the groupby() method on students dataset with the 'female_flag' as argument and assign the returned value to a variable named gender_group
gender_group = students.groupby('female_flag')
## We need to keep in mind that trying to print the gender_group object will only give us a generic memory-based string representation
#print(gender_group)

## Now we want to compute the average GPA of each group in the preceeding grouping
print(gender_group['gpa'].mean())
## The results show that the average GPA of females is 93 and 92,3 for males

## Using the groupby() method and then further using commands on the resulting variable is quite intuitive
## We can also compute the total number of classes attended by male or female students
print(gender_group['num_classes'].sum())