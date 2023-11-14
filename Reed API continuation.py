import pandas as pd
import os

os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Desktop')

reed_df=pd.read_csv('Reed_data_analyst.csv')

uk_homeoff_df=pd.read_csv('2023-11-10_-_Worker_and_Temporary_Worker.csv')

reed_df['employerName']=reed_df['employerName'].str.upper()
uk_homeoff_df['Organisation Name']=uk_homeoff_df['Organisation Name'].str.upper()

result = reed_df[reed_df['employerName'].apply(lambda x: uk_homeoff_df['Organisation Name'].str.contains(x)).any()]

print(result.value_counts())
result.to_csv('result.csv')