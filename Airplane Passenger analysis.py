import pandas as pd
import os
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Recordings/Projects/'/C5 Input for participants/domestic_visitors")
files = os.listdir()
dom_vist_merged = pd.DataFrame()
for i in files:
    df = pd.read_csv(i)
    dom_vist_merged = pd.concat([df, dom_vist_merged])

os.chdir(
    "C:/Users/laksrgan/OneDrive - Keysight Technologies/Recordings/Projects/'/C5 Input for participants/foreign_visitors")
files = os.listdir()
for_vist_merged = pd.DataFrame()
for i in files:
    df = pd.read_csv(i)
    for_vist_merged = pd.concat([df, for_vist_merged])

dom_vist_merged['visitors'] = dom_vist_merged['visitors'].replace(' ', '0')
dom_vist_merged.year = dom_vist_merged.year.astype('int64')
dom_vist_merged.visitors = dom_vist_merged.visitors.astype('float64')
dom_vist_merged['visitors'].fillna(0, inplace=True)
dom_vist_merged_sum = dom_vist_merged.groupby('district').agg(visitor_sum=('visitors', sum)).reset_index()
dom_vist_merged_sum.sort_values(by='visitor_sum', ascending=False, inplace=True)
dom_vist_merged_sum = dom_vist_merged_sum.head(10)
# 1. Top 10 districts with high visitor count
plot = sns.barplot(x='district', y='visitor_sum', data=dom_vist_merged_sum)
plot.set_xticklabels(plot.get_xticklabels(), rotation=30)

# 2. Top 3 districts with growing CAGR
dom_vist_gp = dom_vist_merged.groupby(['district', 'year']).agg(visitor_sum=('visitors', sum)).reset_index()
dom_vist_gp.visitor_sum = dom_vist_gp.visitor_sum.astype('int64')

n_periods = 3

val = dom_vist_gp['district'].drop_duplicates()
lst = dom_vist_gp.columns
df2 = pd.DataFrame()
for i in val:
    df = dom_vist_gp[dom_vist_gp['district'] == i].reset_index()
    df.drop(columns='index', axis=1, inplace=True)
    fv = df['visitor_sum'].iloc[0]
    lv = df['visitor_sum'].iloc[-1]
    cagr = (fv / lv) ** (1 / 3) - 1
    df['CAGR'] = cagr
    df2 = pd.concat([df2, df], axis=0)
df_result = df2[['district', 'CAGR']].reset_index()
df_result.drop(columns='index', inplace=True)
df_result.drop_duplicates(inplace=True)
df_result.sort_values(by='CAGR', ascending=False, inplace=True)
df_result.dropna(axis=0, inplace=True)
# print(df_result.head(3))
# print(df_result.tail(3))

# 4. Peak & Low season months for Hyderabad
merged_df=dom_vist_merged[dom_vist_merged['district']=='Hyderabad']
merged_df1 = merged_df.groupby(['district', 'month']).agg(visit_sum=('visitors', sum)).sort_values(by='visit_sum')
#print(merged_df1)

#5. Top & Bottom 3 districts with domestic to foreign ratio

dom_merged_df = dom_vist_merged.groupby(['district']).agg(visit_sum=('visitors', sum)).sort_values(by='visit_sum').reset_index()
dom_merged_df.visit_sum=dom_merged_df.visit_sum.astype('int64')

for_vist_merged.visitors=for_vist_merged.visitors.replace(' ','0')
for_vist_merged.visitors=for_vist_merged.visitors.astype('int64')
for_merged_df = for_vist_merged.groupby(['district']).agg(visit_sum=('visitors', sum)).sort_values(by='visit_sum').reset_index()

join_df=pd.merge(left=for_merged_df,right=dom_merged_df,on='district',how='inner',suffixes=['_for','_dom'])
join_df['ratio']=join_df['visit_sum_dom']/join_df['visit_sum_for']
join_df.sort_values(by='ratio',ascending=False,inplace=True)
print(join_df)