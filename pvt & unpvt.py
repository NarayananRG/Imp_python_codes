import pandas as pd
import os
import numpy as np

pd.set_option('display.max_columns', 5)

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
df=pd.read_csv("online_retail2.csv")
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape)

print(df.isnull().sum().sum())

df.dropna(axis=0,how='any',inplace=True)
print(df.shape)



df['Date']=pd.to_datetime(df['InvoiceDate'])
print(df.info())

print(df[(df.Country=='Germany') | (df.Country=='France')].Country.value_counts())
countries=['Germany','France']
#print(df[df.Country.isin(countries)])

#print(df[df.Date>='2011 Aug'])

#print(df.groupby(['Country','StockCode']).agg(qty_sum=('Quantity',np.sum),
                                              #price_count=('Price',np.count_nonzero)).reset_index())
country_pvt=df[['Country','StockCode','Quantity','Price']]
print(country_pvt)

pvt_tbl=pd.pivot_table(country_pvt,values=['Quantity','Price'],
                       columns='Country',index='StockCode',aggfunc={'Quantity':np.sum,'Price':np.count_nonzero},fill_value=0).reset_index()
pvt_tbl.columns=pvt_tbl.columns.map('_'.join)
print(pvt_tbl.head(5))

unpvt=pd.melt(pvt_tbl,id_vars=['StockCode_'],var_name=['Measure'])

print(unpvt)