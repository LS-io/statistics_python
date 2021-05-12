## When we want to draw random samples (we have seen how the random library is used for this), we sometimes want to draw for a probability other than then uniform one.
## NumPy has various options in regards to this, e.g. the random.normal for drawing from a normal (Gaussian or the "bell curve") distribution, or similarly from the bernoully or poisson distribution.
## By random sampling a given distribution, we can obtain an actual realisation of the random variable
import numpy as np

sample = np.random.normal()
#print(sample)

## We might be aware that the normal distribution is specified by two parameters, a mean and a standard deviation.
## We can specify them using the loc (default value is 0.0) and scale (default value 1.0)
sample = np.random.normal(loc = 100, scale = 10)
#print(sample)

## It is also possible to draw multiple samples
## We achieve this by specifying the size argument
samples = np.random.normal(loc = 100, scale = 10, size = (6, 3, 3))
#print(samples)


## We need to keep in mind that each probability distribution has its own statistics that define it
## For example, lets look at the Poisson distribution, that is defined by the lambda parameter
samples = np.random.poisson(lam = 10, size = (6, 3, 3))
#print(samples)


## Lastly, NumPy also offers some randomness-related functionality in the random module
## np.random.randint() function returns a random integer between two given numbers
## np.random.choice() randomly draws a sample from a given one-dimensional array
## np.random.shuffle() randomly shuffles a given sequence
print(np.random.randint(low = 0, high = 10, size = (2, 3)))
print('-' * 50)
print(np.random.choice([1, 3, 4, -6], size = (2, 2)))
print('-' * 50)
a = [1, 2, 3, 4]
for _ in range(3):
    np.random.shuffle(a)
    print(a)