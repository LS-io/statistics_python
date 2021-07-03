# Overview of Statistics
So far we have learned the basics of using the Python language and some of the relevant libraries to use in programming or dealing with data.
We have checked NumPy, Pandas, MatPlotLib and Seaborne.
Now, we need to go over statistics, as having a good understanding of it will give us a better insight into how and when different python tools can be used.

In the context of given data (or a given dataset), statistics deals with two objectives - describing the given data and drawing conclusions from it. Hence, the two subfield of use of statistical concepts are called **descriptive statistics** and **inferential statistics**.

Decriptive statistics deals with questions about the general characteristics of a dataset (e.g. the average amount, difference between the maximum and minimum, most common value etc.). These answers cna give us a better understanding of what the dataset in question constitutes and what is the subject of the dataset.

Inferential statistics, on the other hand, deals with extracting the appropriate insights from the given data. Often we wish to make an assumption about the future, based on data presented. In order to do this, different statistical and machine learning models can be used, which can usually only be applied to specific kinds of data.
That is the reason why we need to understand what type(s) of data we have in our dataset.
___
## Types of data in statistics
There are two main types of data in statistics:
* categorical data
* numerical data

In the table below, we can observe the summary of relevant points of difference for the two data types

|Features|Categorical Data|Numerical data|
|---|---|---|
|Characteristic|Discrete values|Continuous values-|
|Ordinality|No|Yes|
|Modelling|Categorical/discrete probability distributions|Continuous probability distributions|
|Data processing|One-hot encoding|Scaling and normalisation|
|Descriptive statistics|Mode|Mean and standard deviation|
|Predictive modelling|Classification|Regression|
|Visualisation techniques|Pie charts and bar graphs|Histograms, Line graphs and scatter plots|
___
### Categorical data
If an attribute or a variable is categorical, its values belong to a predetermined and fixed set of possible values. An example is a weather-related dataset, which could consist of discrete values such as *"sunny"*, *"Windy"*, *"cloudy"*, *"rainy"* and so on. A cell in column of such discrete categorical data **must** take the value of one of these possibilites, and can not contain a number or an unrelated string.

Due to the nature of categorical data, the different possible values are not ordinally related, meaning that there is no clear comparison between one or the other value, whereas in numerical data, they are cleary ordered on a numerical scale.

When it comes to modelling, if a variable with an unknown value belongs to a categorical attribute and is to be modelled with a probability distribution, a categorical distribution will be required. Such a distribution describes the probability that the variable belongs to one of the ***K*** possible categories, that are predefined.

When it comes to data processing, an encoding scheme is typically used to *convert* the values from categorical to numerical, so that they can be interpreted by a machine.

For example, some tend to use a simple scheme of assigning each possible discrete value a positive integer and replacing it in their respective place.
Example below:
```
weather_df

    temp    weather
0   55      windy
1   34      cloudy
2   80      sunny
3   75      rain
4   53      sunny
```
Here, we can use the **map()** method to effectively encode the weather attributes into numerical values
```
weather_df['weather_encoded'] = weather_df['weather'].pam({'windy': 0, 'cloudy': 1, 'sunny': 2, 'rain': 3})
```
```
weather_df

    temp    weather     weather_encoded
0   55      windy       0
1   34      cloudy      1
2   80      sunny       2
3   75      rain        3
4   53      sunny       2
```
We can that the **weather** column has been converted to numerical values in the **weather_encoded** column via one-to-one mapping. The danger with this method is the implied order of numerical values. This can be especially problematic if the model we are using is interpreting this as true numerical data.\
For this reason, we must be careful when transforming our categorical attributes into numerical form.

Another technique we can use is *one-hot-encoding*, which creates a new columnd for every unique value in the column that we want to perform one-hot-encoding on. Then, if the row has the corresponding value in the original attribute columnd, we place a value of 1, if not, then value of 0.\
The example below reiterates how we can implement this in pandas
```
pd.get_dummies(weather_df['weather'])
```
```
    cloudy  rain    sunny   windy
0   0       0       0       1
1   1       0       0       0
2   0       0       1       0
3   0       1       0       0
4   0       0       1       0
```
___
When it come to various descriptive statistical tools, the mode is typically the only statistic that can be used on categorical data.\
In terms of making predictions, if a categorical attribute is the target of our machine learning pipeline (we want to predict a categorical attribute), then classification models are required. Opposed to regression models (which make predictions on numerical, continuous data), classification models (classifiers for short) only predict amon the possible values for the target attribute.

Last big difference between categorical and numerical data is in the visualisation techniques. Two of the most common visualisation techniques for categorical data are bar charts (including stacked and grouped bar charts) and pie charts. They both focus on the portion of the whole dataset that each unique vales takes up.

#### Binary Data
Values in a binary attribute can only be **True** or **False**. It is a categorical attribute whose set of possible values contains the two Boolean values mentioned. Boolean values can easily be interpreted by machine learning and mathematical models, so there is usually no need to convert a binary attribute to any other form.\
To use this feature to its full benefit, we would want to convert any binary data into Boolean values, if it isn't already in that form.\
Example:
```
student_df
```
```
    name    sex     class   gpa num_classes
0   Alice   female  FY      90  4
1   Bob     male    SO      93  3
2   Carol   female  SR      97  4
3   Dan     male    SO      89  4
4   Eli     female  JR      95  3
5   Fran    female  SR      92  2
```
In the example of student_df, we see that the **'sex'** column is categorical attribute whose values can only be either **'female'** or **'male'**. To make this data more machine friendly, we will *binarise* the attribute:
```
student_df['female_flag'] = student_df['sex'] == 'female'
student_df = student_df.drop('sex', axis = 1)
student_df
```
The output is:
```
    name    class   gpa num_classes female_flag
0   Alice   FY      90  4           True
1   Bob     SO      93  3           False
2   Carol   SR      97  4           True
3   Dan     SO      89  4           False
4   Eli     JR      95  3           True
5   Fran    SR      92  2           True
```
*Exercise 301 uses these concepts to look at the weather dataset*
___
### Numerical Data
As opposed to categorical data, numerical data contains numerical and continous values or real numbers. Values can take a specific range (positive, negative, between 0 and 1, etc.) and be of any value in this range. Unlike categorical data, where values can only take one out of discretely given set of possible values.

While few probability distributions are fit to be used with categorical data, there are many different possible distribution we can use to deal with numerical data. Some of them are normal distribution (bell-curve distribution), uniform distribution, exponential distribution, the Student's t distributio and other.\
Each type of distribution is used to represent a different kind of numerical data.\
Normaly distribution, for example, is often used to model quantities with linear growth, such as height, age, test scores and so on, and exponential distributio models the amount of time between the occurences of a given event.

It is therefore important to understand which specific probability distribution is sutiable for the numerical attribute that we wish to model. Choosing the appropriate distribution allows us to perform a coherent analysis as well as make an accurate prediction.

Additionally, different processing techniques can be applied to numerical data. Two most common include scaling and normalisation.\
Scaling involves adding and/or multiplying all the values in a numerical attribute by a fixed quantity to scale the range of original data to another range. This is useful when statistical and machine learning models can only handle values within a given range (as between 0 and 1 for example).

Such often used scaling technique is the min-max scaling method.\
It can be expressed by the following formula, where *a* and *b* are positive numbers:

![\Large X'=a+(b-a)\frac{X-X_{min}}{X_{max}-X_{min}}](https://latex.codecogs.com/svg.image?X^{'}=a&plus;(b-a)\frac{X-X_{min}}{X_{max}-X_{min}})

*X'* and *X* denote the data after and before the transformation, while *X<sub>max</sub>* and *X<sub>min</sub>* dentore the maximum and minimum values within the data respectively. The output of the formula is always greater than *a* and less than *b*.

When it comes to normalisation, it denotes the process of specifically scaling a numerical attribute to the normalised form with respect to its probability distribution. The goal is for us to obtain a transformed dataset that nicely follows the shape of the probability distribution that we have chosen.\
For example, let's say we have data that follows the normal distribution with a mean of **4** and a standard deviation of **10**. If our model assumes that the standard form of the normal distribution for this data is **0** for the mean and **1** for the standard deviation, it will have difficulties learning from it. Hence, we want to apply the normalisation technique for normally distributed data. We subtract the true mean from the data points and divide the result by the true standard deviation. As a scaling process, this is more generally known as a standard scaler.\
In a code cell, given the preceding data is already a NumPy array, we can implement this process as follows:
```
# Creating our samples as preceding data
samples = np.random.normal(4, 10, size = 1000)

# Applying the normalisation technique
normalised_samples = (samples - 4) / 10
```
With this technique, the data has successfully shifted to the range we need (centering around mean = 0) without changing the general shape of the data distribution.\
*As a footnote, in practice when the true mean and true standard deviation are not known, we can help ourselves with an approximation:
```
sample_mean = np.mean(samples)
sample_sd = np.std(samples)
```
When we are dealing with a large number of samples, these two techniques offer a good approximation that can be further used for type of transformation. With this, we can now feed our normalised data to our statistical and machine learning models.

Addressing the mean and the standard deviation, these two statistics are usually used to describe numerical data. To fill in the missing values in a numerical attribute, central tendency measures such as the mean and the median are typically used. In some special cases such as a time-series dataset, you can use more complex missing values imputation techniques such as interpolation, where we estimate the missing value to be somewhere *in between* the ones immediately before and after it in a sequence.

When we want ot train a predictive model to target a numerical attribute, regression models are used. Instead of making predictions on which possible categorical values an entry can take like a classifier, a regression model looks for a reasonable prediciton across a continuous numerical range. As such, similar to what we have discussed, we must make sure to only apply regression models on dataset whose target values are numerical attributes.

In terms of visualising numerical data, we have seen a wide range of visualisation techniques that can be used. Apart from histograms, which can be used to describe the distribution of a numerical attribute, line graphs and scatter plots allow us to visualise patterns of an attribute with respect to other attributes. Additionally, heatmaps are used to visualise a 2-dimensional structure which can be applied to represent correlation between numerical attributes in a dataset.

### Ordinal Data