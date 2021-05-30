## Let's use our skils from datavisualisation.py

## We will compare the sampling functions of NumPy against their true probability distributions
## For this exercise, we will need the NumPy, SciPy and MatPlotLib packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# let's start by drawing 1000 samples from the normal distribution
samples = np.random.normal(0, 1, size = 1000)

# Next, we call the np.linspace() function to create and array between the minimum and maximum of the samples
x = np.linspace(samples.min(), samples.max(), 1000)
y = stats.norm.pdf(x)

# We will now create a histogram for the drawn samples
plt.hist(samples, alpha = 0.2, bins = 20, density = True)
plt.plot(x, y)
plt.show()

# In the next step, let's create the same visualisation for the Beta distribution with the parameters (2, 5)
samples = np.random.beta(2, 5, size = 1000)
x = np.linspace(samples.min(), samples.max(), 1000)
y = stats.beta.pdf(x, 2, 5)

plt.hist(samples, alpha = 0.2, bins = 20, density = True)
plt.plot(x, y)
plt.show()

# And finally, for the gamma distribution
samples = np.random.gamma(1, size = 1000)
x = np.linspace(samples.min(), samples.max(), 1000)
y = stats.gamma.pdf(x, 1)

plt.hist(samples, alpha = 0.2, bins = 20, density = True)
plt.plot(x, y)
plt.show()