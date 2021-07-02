## We start with importing the packages we will be using
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather_df = pd.read_csv('B:/Coding/Github/statistics_python/chapter3_pystatisticaltoolbox/exercise301_data/weather_data.csv')
##Remove the full filepath before committing
#print(weather_df.head(10))

## We see that the dataset tells us what the weather was on a given day in a given city
# weather_df['weather'].value_counts().plot.bar()
# plt.show()

## Let's visualise the same information in a pie chart
# weather_df['weather'].value_counts().plot.pie(autopct = '%1.1f%%')
# plt.ylabel('')
# plt.show()

## Now we will visualise these counts of weather types together with the information on what percentage each weather type accounts for in each city.
#print(weather_df.groupby(['weather', 'city'])['weather'].count().unstack('city'))
## In places where we have a NaN, there are no occurences of that type of weather

## Now we will visualise this data in a stacked bar plot
weather_df.groupby(['weather', 'city'])['weather'].count().unstack('city').fillna(0).plot(kind = 'bar', stacked = True)
plt.show()