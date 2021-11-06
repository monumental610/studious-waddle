import requests # to get data from api
import json # to convert json file to dict

response = requests.get("https://api.wazirx.com/api/v2/market-status") # gets data from wazirx in 'response' type data
#print(response.status_code)
data = json.loads(response.text) #converts 'response' type data to python 'dict'
#print(type(data))
#print(data['assets']) # part which is under use
deposit = None
withdrawal = None
for asset in data['assets']:
    if asset['deposit'] == 'enabled':
       deposit = asset['type'] #prints codename of the coin ada,btc etc
       print(str(deposit))     #prints coins which have deposit enabled
print("enjfjghghfkdd")
for asset in data['assets']:
    if asset['withdrawal'] == 'enabled':
       withdrawal = asset['type'] #prints codename of the coin ada,btc etc
       print(str(withdrawal))     #prints coins which have withdrawal enabled