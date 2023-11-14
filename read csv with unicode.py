#collect multiple files
import pandas as pd
import os
os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Recordings\New folder\additional_data')
files=os.listdir()

df1=pd.DataFrame()
for i in files:
    if i.endswith('.csv'):
        try:
            df=pd.read_csv(i,encoding='utf-8')
            df1=pd.concat([df,df1],axis=0)
        except UnicodeDecodeError:
            print(f'file error {i}')
            df = pd.read_csv(i, encoding='latin-1')
            df1=pd.concat([df,df1],axis=0)

df1.drop_duplicates(inplace=True)
df1.to_csv('edit.csv')