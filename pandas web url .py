import re
from io import StringIO

import pandas as pd

item = 'a!b@c#â€'

# Remove all symbols from the string
item = re.sub(r'[^\x00-\x7F]', '', item)
item = re.sub(r'[^\w\s]', '', item)
# Print the string
print(item)


dictt={1:'one',2:'two',3:'three'}

dictt[4]='four'
print(dictt.keys(),dictt.values())

data=('col1,col2\n''1,2\n''3,4\n')
df=StringIO(data)
csv=pd.read_csv(df,dtype=object)
print(csv.info())

url='https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

df=pd.read_html(url)
print(df)
col=['OrgId',
'Name',
'CageCode',
'DUNSNum',
'PhoneNum',
'FaxNum',
'WebSite',
'State',
'Descrip',
'Address',
'PostalCode',
'Country',
'Comments',
'CreateDate',
'UpdateDate',
'MDREmails',
'ParentManu',
'sTSOESData',
'sAMCData']

df11=pd.read_csv("C:/Users/laksrgan/OneDrive - Keysight Technologies/Documents/Company_extract_20230922073051.dat",delimiter='|')
df11.columns=col
#print(df11.head(5))

#df11.drop(index=False,inplace=True)
#print(df11.head(5))

cmp_ext_file_msg='Company_extract_20230922073051.dat'

print(cmp_ext_file_msg.replace('.dat','.csv'))