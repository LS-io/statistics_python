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

for curve, color, style in zip(curves, colors, styles):
    plt.plot(x, curve, c = color, linestyle = style)

plt.show()