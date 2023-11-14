import pandas as pd
import os
os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

df=pd.read_csv("online_retail2.csv")
#print(df.iloc[0:5,0:5])

df['Price_USD']=df['Price']*82

lst=['a','b','c']

def findd(charr):
    if charr=='a':
        print(charr)
    elif charr=='b':
        print(charr)
    else:
        print('Out of Alphabets')

res=map(findd,lst)
print(list(res))

def countries(inp):
    if inp =='United Kingdom':
        return True
    else:
        return False
    
df['ukornot']=df['Country'].map(countries)
print(df)
print(df.columns)