import requests # to get data from api
import json # to convert json file to dict

def Stringinize(string):     #seperate string data into seperated list data
    li = list(string.split(" "))
    return li

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
        #depositstring = Stringinize(deposit)
        #print(type(depositstring))     #prints coins which have deposit enabled in seperated list form
        symboldeposit = deposit + "USDT"
        depositsymbol = symboldeposit.upper() 
        print(depositsymbol) #prints out coin pairs to be given to binance in uppercase letter
        

for asset in data['assets']:
    if asset['withdrawal'] == 'enabled':
        withdrawal = asset['type'] #prints codename of the coin ada,btc etc
        #withdrawalstring = Stringinize(withdrawal) 
        #print(type(withdrawalstring)) #prints coins which have withdrawal enabled in seperated list form
        symbolwithdrawal = withdrawal + "USDT"
        withdrawalsymbol = symbolwithdrawal.upper()
        print(withdrawalsymbol) #prints out coin pairs to be given to wazirx in uppercase letter
       

#symbolprice = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT")
