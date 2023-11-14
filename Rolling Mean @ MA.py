from matplotlib import pyplot as plt
import pandas as pd
import os
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
df=pd.read_csv("stocks.csv",parse_dates=True)
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
resample_mean=df.resample('M').mean()

msft=df[['MSFT']]
msft['Rolling_Mean']=msft.rolling(window=7).mean()
print(msft)
msft['2000-01-03':'2000-05-03'].plot()
plt.show()