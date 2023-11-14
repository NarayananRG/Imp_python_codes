import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import os
from datetime import datetime as dt
import numpy as np
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
twll=pd.read_csv('twel.csv')

df=twll[twll['Country'].isin(['United Kingdom','Canada','Denmark','EIRE'])]
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
df['date']=df['InvoiceDate'].dt.strftime('%Y-%m')

"""
df_grouped=df.groupby(['date','Country']).agg(total_sales=('Quantity',np.sum)).reset_index()
uk=df_grouped[df_grouped['Country'].isin(['United Kingdom'])][['total_sales','date']]

can=df_grouped[df_grouped['Country'].isin(['Canada'])][['total_sales','date']]
den=df_grouped[df_grouped['Country'].isin(['Denmark'])][['total_sales','date']]
irl=df_grouped[df_grouped['Country'].isin(['EIRE'])][['total_sales','date']]


plt.subplot(2,2,1)
plt.plot(uk.date,uk.total_sales)
plt.subplot(2,2,2)
plt.plot(can.date,can.total_sales)
plt.subplot(2,2,3)
plt.plot(den.date,den.total_sales)
plt.subplot(2,2,4)
plt.plot(irl.date,irl.total_sales)
plt.tight_layout()
plt.show()


cars=pd.read_csv('cars.csv')
sns.scatterplot(cars,x='horsepower',y='Price')
plt.show()
"""
cars=pd.read_csv('cars.csv')

car_df=cars[cars['cylenders'].isin([4,6,8])]

sns.boxplot(data=car_df,x='cylenders',y='horsepower',hue='cylenders')
plt.show()
