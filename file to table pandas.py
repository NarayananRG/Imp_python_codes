import pandas as pd
import os

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Documents/")
"""csv=pd.read_csv("IM35.csv",index_col=0,usecols=range(1,4))
csv.dropna(axis=1,inplace=True)
print(csv.head(10))

excel=pd.read_excel("Incorta.xlsx",sheet_name='Sheet3',index_col=0)
#excel.dropna(axis=1,inplace=True)
print(excel.head(10))"""

txt=pd.read_table("IM81NEW.txt",delimiter=',',index_col=0)
filt=txt[txt['Item Number']=='MXR608A-ATO-1767']
print(filt['Description'])