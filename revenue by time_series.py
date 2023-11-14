import pandas as pd
import os
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

ors=pd.read_csv('retail_clean.csv')
ors.InvoiceDate=pd.to_datetime(ors.InvoiceDate)
ors['week']=ors.InvoiceDate.dt.strftime('%U')
ors['month']=ors.InvoiceDate.dt.month
ors['year']=ors.InvoiceDate.dt.year
ors['date']=ors.InvoiceDate.dt.strftime('%Y-%m-%d')
ors['revenue']=ors.Price * ors.Quantity
ors_gp=ors.groupby(['week','month','year']).agg(date=('date','first'),
                                                total_revenue=('revenue',np.sum)).reset_index().sort_values(by='date')
print(ors_gp)
ors_gp.to_csv('time_series.csv',index=False)
sns.lineplot(x='date',y='total_revenue',data=ors_gp)
plt.show()