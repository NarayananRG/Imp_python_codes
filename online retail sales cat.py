import pandas as pd
import os
import numpy as np

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")
retail = pd.read_csv('online_retail2.csv')

retail.dropna(axis=0, how='any', inplace=True)
retail.drop_duplicates(inplace=True)
retail_clean = retail[retail.Quantity > 0]
retail_clean['revenue'] = retail.Quantity * retail.Price
retail_clean_gp = retail_clean.groupby(['Description', 'StockCode']).agg(
    total_sales=('Quantity', np.sum),
    total_revenue=('revenue', np.sum)
).reset_index()
# retail_clean_gp.to_csv('abc_analysis.csv',index=False)
retail_clean_gp.sort_values(by='total_sales', inplace=True)
retail_clean_gp['sales percent'] = (retail_clean_gp.total_sales / sum(retail_clean_gp['total_sales'])) * 100
retail_clean_gp['cumu sales perc'] = round(retail_clean_gp['sales percent'].cumsum(axis=0))
retail_clean_gp['cumu sales perc'] = retail_clean_gp['cumu sales perc'].astype('int64')
print(retail_clean_gp.info())


def categ(perc):
    if perc <= 75:
        return 'A'
    elif perc <= 95:
        return 'B'
    elif perc > 95:
        return 'C'
    else:
        return 'NA'


retail_clean_gp['category'] = retail_clean_gp['cumu sales perc'].map(categ)

print(retail_clean_gp['category'].value_counts())
