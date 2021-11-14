import requests # to get data from api
import json # to convert json file to dict
import time # to see performance time

response = requests.get("https://api.wazirx.com/api/v2/market-status") # gets data from wazirx in 'response' type data
#print(response.status_code)
data = json.loads(response.text) #converts 'response' type data to python 'dict'
#print(type(data))
#print(data['assets']) # part which is under use

for asset in data['assets']:
    if asset['deposit'] == 'enabled':
        deposit = asset['type'] #prints codename of the coin ada,btc etc
        symboldeposit = "https://api.binance.com/api/v3/ticker/price?symbol=" + deposit.upper() + "USDT"
        #print(symboldeposit) #prints out coin pair links to be given to binance 
        responsedepositsymbolprice = requests.get(symboldeposit) #GETS symbol price
        #print(responsedepositsymbolprice.status_code)
        depositsymbolprice = json.loads(responsedepositsymbolprice.text)
        #print(type(depositsymbolprice))
        #print(depositsymbolprice)
        if responsedepositsymbolprice.status_code == 200 : #if symbolpair is correct goes to next step
            print(depositsymbolprice)
print("yes")
for asset in data['assets']:
    if asset['withdrawal'] == 'enabled':
        withdrawal = asset['type'] #prints codename of the coin ada,btc etc
        symbolwithdrawal = "https://api.wazirx.com/uapi/v1/ticker/24hr?symbol=" + withdrawal + "usdt"
        #print(symbolwithdrawal) #prints out coin pair links to be given to binance 
        responsewithdrawalsymbolprice = requests.get(symbolwithdrawal) #GETS symbol price
        #print(responsewithdrawalsymbolprice.status_code)
        withdrawalsymbolprice = json.loads(responsewithdrawalsymbolprice.text)
        #print(type(withdrawalsymbolprice))
        #print(withdrawalsymbolprice)
        if responsewithdrawalsymbolprice.status_code == 200 : #if symbolpair is correct goes to next step
            print(withdrawalsymbolprice['lastPrice'])

print(time.process_time()) # to see code performance time
