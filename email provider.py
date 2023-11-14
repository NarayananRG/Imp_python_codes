import os
import pandas as pd
#pd.set_option('display.max_columns',None)
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies\Downloads\Archive")

df1=pd.read_csv("Ecommerce_Purchases",delimiter=',',doublequote="")

#df1.to_csv("ecom_purch.csv")
print(df1.isnull().sum())
print(df1['Purchase Price'].mean())
print(df1[df1['Language']=='fr']['Language'].count())
print(df1[df1['Job'].str.contains('engineer',case=False)]['Job'].count())

print(df1[df1['IP Address'].str.contains('132.207.160.22',case=False)]['Email'])

print(df1[(df1['CC Provider']=='Mastercard') & (df1['Purchase Price']>50)])

print(df1['AM or PM'].value_counts())

df1['CC Exp Date']=pd.to_datetime(df1['CC Exp Date'],format='%m/%y')
df1['year']=df1['CC Exp Date'].dt.strftime('%Y')
print(df1[df1['year']=='2020']['year'].count())

lst=[]
def email(a):
    b=a.split('@')[1]
    lst.append(b)
    return b
df1['prov']=df1['Email'].apply(lambda x: x.split('@')[1])
df1['email_prov']=df1['Email'].map(email)
print(df1['email_prov'].value_counts().head(3))
print(df1['prov'].value_counts().head(3))