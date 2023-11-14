import pandas as pd
import os
import numpy as np
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

#pd.set_option('display.max_rows',None)

flights=pd.read_csv('flights.csv')
airports=pd.read_csv('airports.csv')
airlines=pd.read_csv('airlines.csv')
print(flights.columns)

#df=pd.merge(flights,airports,how='inner',right_on='faa',left_on='origin')
#print(df[['dest','origin','tzone']])
#df=flights[flights.origin=='NewYork']
#print(df)

print(flights.month.value_counts())
#flights.info()
#punct=flights[(flights.dep_delay==0) & (flights.arr_delay==0)][['dep_delay','arr_delay','carrier']]

flights['total_delay']=flights['dep_delay']+flights['arr_delay']

#punct=flights.groupby('carrier').agg(delay_mean=('total_delay',np.mean))

#punct_air=pd.merge(punct,airlines,how='left',left_on='carrier',right_on='carrier').sort_values(by='delay_mean',)
#print(punct_air.drop_duplicates())
punct=flights.groupby(['carrier','dest','origin']).agg(air_time_max=('air_time',np.max)).reset_index()
punct.sort_values(by='air_time_max',ascending=False,inplace=True)


print(punct)