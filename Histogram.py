import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies\Downloads")
csv=pd.read_csv("ToyotaCorolla.csv",na_values=['??','???'])
#csv.dropna(axis=0,inplace=True)

csv=csv.apply(lambda x : x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))


print(csv.isnull().sum())

missing=csv[csv.isnull().any(axis=1)]
csv['Price'].fillna(csv['Price'].mean(),inplace=True)
csv['Age']=csv['Age'].fillna(csv['Age'].mean())
csv['KM'].fillna(csv['KM'].median(),inplace=True)
csv['HP'].fillna(csv['HP'].mean(),inplace=True)
csv['FuelType'].fillna(csv['FuelType'].value_counts().index[0],inplace=True)
csv['MetColor'].fillna(csv['MetColor'].mode().index[0],inplace=True)
csv['Automatic'].fillna(csv['Automatic'].mode().index[0],inplace=True)
csv['CC'].fillna(csv['CC'].mean(),inplace=True)
csv['Doors'].fillna(csv['Doors'].value_counts().index[0],inplace=True)
csv['Weight'].fillna(csv['Weight'].median(),inplace=True)

"""filterd_csv=csv[csv['KM']<20000000]
print(filterd_csv.head(50))
plt.scatter(csv['Age'],csv['Price'],c='red')
plt.xlabel('Age')
plt.ylabel('Price')
plt.title('Price Vs Age Correlation')

plt.hist(filterd_csv['KM'],color='green',edgecolor='white',bins=5)
plt.show()"""