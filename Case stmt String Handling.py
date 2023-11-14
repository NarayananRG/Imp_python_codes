import pandas as pd
import re

dict = {'col1': [
'MSM Supplier Code: 04723 DO NOT USE - MERGED TO ATOTECH',
'MSM Supplier Code: 04724',
'MSM Supplier Code: 04725',
'MSM Supplier Code: 04739 Isha: Web Form Filled  E-mail IDs from this url:  http://yosemite.epa.gov/r10/nplpad.nsf/e144fa5b179a8a0388256365007ef6eb/39dd3205823cb6c785256595004b0ea3?OpenDocument',
'MSM Supplier Code: 04741 pnegrin@muellerelectric.com; jeffkulp@muellerelectric.com; briemer@muellerelectric.com; Julia Shumulinsky [jshumuli@muellerelectric.com];   For sales contact:http://www.muellerelectric.com/pdf/SalesContacts.pdf Muell',
'MSM Supplier Code: 04767 Manoj:- Web form filled.',
'MSM Supplier Code: 04770 DO NOT USE - MFR NAME CHANGED TO PERMATEX'
], 'col2': [1, 2, 3, 4, 5,6,7]}

df = pd.DataFrame(dict)
print(df)

def str_manup(string):
    for i in range(0,10,1):
        substring = "MSM Supplier Code:"
        index = string.find(substring) +18
        a=string[index:index+10]
        b=a.lstrip()
        c=b[i]
        if c != re.search(pattern=r'\d',string=c):
            return "'"
        else:
            return c

df['MSM_SUPP_CD']=df['col1'].map(str_manup)

print(df)