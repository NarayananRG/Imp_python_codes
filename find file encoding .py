import pandas as pd
import os
import chardet

os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Recordings\New folder\additional_data')
file='KRvideos.csv'
with open(file,'rb') as f:
    result=chardet.detect(f.read(10000))
    encodingg=result['encoding']
    print(encodingg)


df=pd.read_csv('KRvideos.csv',delimiter=',',encoding='latin-1')
print(df)