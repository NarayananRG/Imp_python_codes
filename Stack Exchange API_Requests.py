import requests
import json
import pprint

"""url='http://api.tvmaze.com/singlesearch/shows'
param={'q':'show'}

response=requests.get(url,params=param)

if response.status_code==200:
    print(response.text)
    data=json.loads(response.text)
    #pprint.pprint(data)
    name=data['name']
    print(name)

else:
    print(response.status_code)
"""
response=requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
data=response.json()
for i in data['items']:
    print(i['title'])
    print(i['link'])
    print()
