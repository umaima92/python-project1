

import pandas as pd
data= pd.read_csv('/Superstore_upd.csv')
data

data.info()

null_values = data.isnull().sum()
print("Null values in each column:")
print(null_values)

data.describe()

data.columns

data[['Sales', 'Quantity', 'Discount', 'Profit']].median()

import matplotlib.pyplot as plt

graph= data.head(20)
graph.plot(x='State', y='Sales')

graph= data.head(20)
graph.plot.bar(x='State', y='Sales')

graph= data.tail(20)
graph.plot(x='State', y='Sales')

graph= data.tail(20)
graph.plot.scatter(x='State', y='Sales')
