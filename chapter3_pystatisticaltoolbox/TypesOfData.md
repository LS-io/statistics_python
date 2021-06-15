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