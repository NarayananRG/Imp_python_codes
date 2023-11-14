import requests
import json
import pandas as pd
import os

os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Desktop')
param = {
    'keywords': 'Data Analyst',
    'location': 'United Kingdom'
}
url = 'https://www.reed.co.uk/api/1.0/search'
response = requests.get(url, params=param, auth=('fcbb5a68-a283-44ee-9294-49cbb0c8a246', ''))
data = response.text
js_tot = json.loads(data)
df_tot = js_tot['totalResults']
print(f"Total Rows : {df_tot}")

df1 = pd.DataFrame()
for i in range(0,df_tot,100):
    param = {
        'keywords': 'Data Analyst',
        'location': 'United Kingdom',
        'resultsToTake': 200,
        'resultsToSkip': i
    }
    print(param)
    response = requests.get(url, params=param, auth=('fcbb5a68-a283-44ee-9294-49cbb0c8a246', ''))
    data = response.text
    js_df = json.loads(data)
    df = pd.DataFrame(js_df['results'])
    df1=pd.concat([df,df1],axis=0)


print(df1)
df1.drop_duplicates()
df1.to_csv('Reed_data_analyst.csv')