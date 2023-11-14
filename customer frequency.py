import numpy as np
import pandas as pd
import os
from datetime import datetime as dt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
df=pd.read_csv("online_retail2.csv")


"""
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
#print(df['InvoiceDate'].dt.month)

#print(df['InvoiceDate'].dt.strftime('%W %Y'))

#print(df['InvoiceDate'].max()-df['InvoiceDate'].min())

recent_df=df.groupby('Customer ID').agg(max_purc_dt=('InvoiceDate',max)).reset_index()
print(recent_df.columns)
recent_df['Customer ID']=recent_df['Customer ID'].astype('int64')
max_inv_date=df['InvoiceDate'].max()

recent_df['dt_diff']=max_inv_date-recent_df['max_purc_dt']
recent_df['dt_diff']=recent_df['dt_diff'].dt.components['days']

from matplotlib import pyplot as plt

plt.hist(recent_df['dt_diff'])
#plt.show()
#print(recent_df)
"""

df.reset_index(inplace=True)
inter_dt=df[['Customer ID','InvoiceDate']].sort_values(by='Customer ID',ascending=True)
inter_dt.dropna(axis=0,how='any',inplace=True)
inter_dt.InvoiceDate=pd.to_datetime(inter_dt.InvoiceDate)
inter_dt['date']=inter_dt['InvoiceDate'].dt.strftime('%Y-%m-%d')
inter_dt_df=inter_dt.iloc[0:500]
inter_dt_shift=pd.DataFrame()

customers=np.unique(inter_dt_df['Customer ID'])
for i in customers:
    cd=inter_dt_df[inter_dt_df['Customer ID']==i]
    cd['prev_date']=cd['date'].shift(1)
    inter_dt_shift=pd.concat([inter_dt_shift,cd],axis=0)

inter_dt_shift['prev_date']=pd.to_datetime(inter_dt_shift['prev_date'])
inter_dt_shift['date']=pd.to_datetime(inter_dt_shift['date'])
inter_dt_shift['prev_date']=inter_dt_shift['date']-inter_dt_shift['prev_date']
inter_dt_shift['prev_date']=inter_dt_shift['prev_date'].dt.components['days']
inter_dt_grp=inter_dt_shift.groupby('Customer ID').agg(mean_prev_days=('prev_date',np.mean))
print(inter_dt_shift)
print(inter_dt_grp)
