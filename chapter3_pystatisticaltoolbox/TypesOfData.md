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
When it come to various descriptive statistical tools, the mode is typically the only statistic that can be used on categorical data.