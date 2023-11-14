import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

df = pd.read_csv("cars.csv").dropna(axis=0)
print(df.shape)
print(df.columns)
print(df['cylenders'].value_counts())

print(np.average(df['horsepower']))
print(np.max(df['horsepower']))
max_price = np.max(df['Price'])
exp_car = df.loc[df['Price'] == max_price]['name']
print(exp_car)

df.rename(columns={'name': 'car_name'}, inplace=True)
print(df.columns)
col = ['car_name', 'Price']
car_price = df.loc[0:, col]
print(car_price)


def car_cat(price):
    if price <= 20000:
        return 'Budget Car'
    elif price > 20000 & price <= 35000:
        return 'Suitable Car'
    elif price > 35000:
        return 'Expensive Car'
    else:
        return 'None'


car_price['car_category']=car_price['Price'].map(car_cat)
print(car_price['car_category'].value_counts())

print(df.columns)
b=df.iloc[:,[8,12,13,15,17]]
print(b.corr())
data=b.loc[0:,['horsepower','weight']]
#sns.heatmap(b.corr())
#plt.show()

def outliers(x):
    first = np.percentile(x, 25)
    third = np.percentile(x, 75)
    iqr = third - first
    upp_thrsh = first + 1.5 * iqr
    low_thrsh = third - 1.5 * iqr
    return upp_thrsh, low_thrsh
print(outliers(df['Price']))

price_dict={'Demand':[400,380,370,390,395,410],'Price':[10,12,13,11,10.5,9]}

df1=pd.DataFrame(price_dict)
x=df1.Price.values.reshape(-1,1)
y=df1.Demand
model=LinearRegression()
print(df1)
model.fit(x,y)
df=df1[['Demand','Price']].sort_values(by=['Demand'],ascending=True)
print(model.coef_)
print(model.intercept_)
df1['Demand Prediction']=model.predict(x)

print(df1)
print(df1.corr())
sns.lineplot(df1)
plt.show()