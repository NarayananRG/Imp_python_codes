import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import numpy as np
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
"""
df=pd.read_csv('stocks.csv')
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
#sns.lineplot(x='Date',y='AAPL',data=df)
#df.plot()
#plt.show()

#scatter plot
cars=pd.read_csv('cars.csv')
#print(cars.cylenders.value_counts())
cars_filt=cars[cars['cylenders'].isin([6,4,8])]
cars_filt['cylenders']=cars_filt['cylenders'].astype('category')
sns.scatterplot(x='horsepower',y='city_miles_per_galloon',data=cars_filt,hue='cylenders')
#plt.show()

#count plot
retail=pd.read_csv('online_retail2.csv')
retail.dropna(axis=0,how='any',inplace=True)
retail.drop_duplicates(inplace=True)
retail_filt=retail[retail['Country'].isin(['France','Portugal'])]
#print(retail_filt['Country'].value_counts())
sns.countplot(data=retail_filt,x='Country')
#plt.show()
retail_filt['InvoiceDate']=pd.to_datetime(retail_filt['InvoiceDate'])
retail_filt['day_of_week']=retail_filt['InvoiceDate'].dt.strftime('%A')
retail_filt['day_of_week_num']=retail_filt['InvoiceDate'].dt.dayofweek
retail_grouped=retail_filt.groupby(['Country','day_of_week','day_of_week_num']).agg(total_qty=('Quantity',np.sum)).reset_index().sort_values(by='day_of_week_num')
retail_grouped=retail_grouped[retail_grouped['total_qty']>=0]
print(retail_grouped)

sns.barplot(x='day_of_week',y='total_qty',data=retail_grouped,hue='Country')
plt.show()
"""

iris=pd.read_csv('iris.csv')

#sns.kdeplot(data=iris,x='sepal_length')
print(iris.species.value_counts())
#sns.kdeplot(data=iris[iris['species']=='setosa'],x='sepal_length')
#sns.kdeplot(data=iris[iris['species']=='versicolor'],x='sepal_length')
#sns.kdeplot(data=iris[iris['species']=='virginica'],x='sepal_length')

#box plot
#sns.boxplot(x='species',y='sepal_length',data=iris)

#histogram
#sns.histplot(x='sepal_length',data=iris,bins=30)

#pariplot
sns.pairplot(iris,hue='species')
plt.show()
print(iris)