import pandas as pd
import os
import seaborn as sns
from matplotlib import pyplot as plt

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

supp = pd.read_csv('supplier_data.csv').reset_index()

supp['risk_profile'] = supp['availability'] + supp['no_suppliers'] + supp['standard'] + supp['price_fluctuation']
supp['value'] = supp['Quantity'] * supp['price']


def category(x, y):
    if (x >= 3000000) & (y >= 1):
        return 'strategic'
    elif (x >= 3000000) & (y < 1):
        return 'leverage'
    elif (x < 3000000) & (y >= 1):
        return 'critical'
    elif (x < 3000000) & (y < 1):
        return 'routine'


for i in range(supp.shape[0]):
    supp.loc[i, 'category'] = category(supp.loc[i, 'value'], supp.loc[i, 'risk_profile'])

print(supp.value_counts())

sns.scatterplot(x='value',y='risk_profile',data=supp,hue='category')
plt.show()