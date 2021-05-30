## We will start with installing the required packages for our visualisation
# !pip install matplotlib seaborn --update --quiet

## Next we need to import the package for us to use it.
## The main workhorse of visualisation functionality in Python is the pyplot package.
import matplotlib.pyplot as plt

#####################################################################################
##
## Scatter plots
##
## The scatter plot is one of the most fundamental visualisation methods.
## It plots a list of points on a plane (or any other higer dimensional space).
## This is done with the plt.scatter() function, as we will test now
x = [1, 2, 3, 1.5, 2]
y = [-1, 5, 2, 3, 0]

#plt.scatter(x, y)
#plt.show()

## We can specify additional arguments in the plt.scatter() function
## e.g. specify the individual points, and colors
sizes = [10, 40, 60, 80, 100]
colors = ['r', 'b', 'y', 'g', 'k']

#plt.scatter(x, y, s = sizes, c = colors)
#plt.show()

#####################################################################################
##
## Line Graphs
## Now let's take a look at plotting graphs with points represented along a curve
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)

#plt.plot(x, y)
#plt.show()

## Similarly as with the scatter plot, we can customise various elements on our line graphs
x = np.linspace(1, 10, 1000)
linear_line = x
log_curve = np.log(x)
sin_wave = np.sin(x)

curves = [linear_line, log_curve, sin_wave]
colors = ['k', 'r', 'b']
styles = ['-', '--', ':']

# for curve, color, style in zip(curves, colors, styles):
#     plt.plot(x, curve, c = color, linestyle = style)

#plt.show()


#####################################################################################
##
## Bar Graphs
## If line graphs are used to represent the trend of a specific function, bar graphs are used to visualise and/or represent the counts of unique values in a dataset through the height of individual bars

labels = ['Type 1', 'Type 2', 'Type 3']
counts = [2, 3, 5]

#plt.bar(labels, counts)
#plt.show()

## As always, we can customise the visual aspect of our graph
## One interesting use is creating the stacked or grouped graphs
type_1 = [1, 1] # 1 of type A and 1 of type B
type_2 = [1, 2] # 1 of type A and 2 of type B
type_3 = [2, 3] #2 of type A and 3 of type B

counts = [type_1, type_2, type_3]
# first, we specify the individual locations of the grouped bars and their width
locations = np.array([0, 1, 2])
width = 0.3
# with the plt.bar() method, we call the appropriate data for the graph, once for the Type A values and once for the Type B values
#bars_a = plt.bar(locations - width / 2, [my_type[0] for my_type in counts], width = width)
#bars_b = plt.bar(locations + width / 2, [my_type[1] for my_type in counts], width = width)
# then, we customise the labels for each group of bars
#plt.xticks(locations, ['Type 1', 'Type 2', 'Type 3'])
#plt.legend([bars_a, bars_b], ['Type A', 'Type B'])
# display the graph
#plt.show()

## To create a stacked bar graph, we use the bottom argument in the plt.bar
#bars_a = plt.bar(locations, [my_type[0] for my_type in counts])
#bars_b = plt.bar(locations, [my_type[1] for my_type in counts], bottom = [my_type[0] for my_type in counts])

#plt.xticks(locations, ['Type 1', 'Type 2', 'Type 3'])
#plt.legend([bars_a, bars_b], ['Type A', 'Type B'])

#plt.show()


#####################################################################################
##
## Histograms
## A histogram us usually used to represent the distribution of values within and attribute (a numeric one)
x = np.random.randn(100)

#plt.hist(x)
#plt.show()

# We can specify the bins argument in order to customise the number of bars that are generated
#plt.hist(x, bins = 100)
#plt.show()
# This visualisation is somewhat worse, as it forces our graph to become fragmented

# Another cool usecase for a histogram is to help compare the distributions of more than one attribute
y = np. random.rand(100) * 4 + 5

#plt.hist(x, color = 'b', bins = 20, alpha = 0.2)
#plt.hist(y, color = 'r', bins = 20, alpha = 0.2)
#plt.show()

# Useful fact to know is that when we simply call the plt.hist() method, a tuple is returned, that contains two arrays of numbers, denoting the locations and heights
#print(plt.hist(x))


#####################################################################################
##
## Heatmaps
## Finally, heatmaps are generated with a 2D array of numbers, where high numbers are represented by hot colors, and vice-versa, low numbers are represented with cold colors
my_map = np.random.rand(10, 10)

#plt.imshow(my_map)
#plt.colorbar()
#plt.show()

# An important use of heatmaps is when we consider the correlation matrix of a dataset. A heatmap can help us pinpoint highly correlated attributes