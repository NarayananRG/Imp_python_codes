import pandas as pd
import os
import numpy as np
from datetime import datetime as dt
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

df=pd.read_csv('twel.csv')
df.drop_duplicates()
#print(df.columns)

df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])

df['week']=df['InvoiceDate'].dt.strftime('%W')
df['day_week']=df['InvoiceDate'].dt.strftime('%W-%a')
df['month']=df['InvoiceDate'].dt.strftime('%m')
df['year_inv_dt']=df['InvoiceDate'].dt.strftime('%Y')
df['month_year']=df['InvoiceDate'].dt.strftime('%m-%Y')
df['date_inv']=df['InvoiceDate'].dt.strftime('%Y-%m-%d')
#print(df[['InvoiceDate','day_week','week','month','year_inv_dt','month_year']])
"""
grouped_df=df.groupby('Customer ID').agg(max_dt_cust=('InvoiceDate',np.max))
cust=np.unique(df['Customer ID'])
#print(df[['Customer ID','InvoiceDate','date']])
df.sort_values(by='Customer ID',inplace=True)
df1=df[['Customer ID','date_inv']].iloc[0:50000]
df1.dropna(axis=0,how='any',inplace=True)
df1=df1.drop_duplicates()
df1.reset_index(drop=True,inplace=True)

shift_df=pd.DataFrame()


for i in cust:
    cd=df1[df1['Customer ID']==i]
    cd['prev_date']=cd['date_inv'].shift(1)
    shift_df=pd.concat([shift_df,cd],axis=0)
shift_df['date_inv']=pd.to_datetime(shift_df['date_inv'])
shift_df['prev_date']=pd.to_datetime(shift_df['prev_date'])
shift_df['recency']=shift_df['date_inv']-shift_df['prev_date']
shift_df['recency']=shift_df['recency'].dt.components['days']
recency=shift_df.groupby('Customer ID').agg(mean_recency_days=('recency',np.mean))
"""
rolling_df=df[['revenue','InvoiceDate']]
rolling_df.set_index('InvoiceDate',inplace=True)
rolling_df['rolling_mean_7']=rolling_df.rolling(window=7).mean()
rolling_df['rolling_mean_14']=rolling_df['revenue'].rolling(window=14).mean()
resample_sum=rolling_df.resample('W').sum()
print(resample_sum)
resample_sum.plot()
plt.show()