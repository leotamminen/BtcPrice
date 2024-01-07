import time
from tqdm import tqdm
import apikey
import requests

# https://coinmarketcap.com/ api key. documentation https://coinmarketcap.com/api/documentation/v1/
# Using apikey.py file to store the api key in the variable "key".
# print(apikey.key)

headers = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts' : 'application/json'
}

params = {
    'start' : '1',
    'limit' : '5',
    'convert' : 'EUR'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

print("Prices for BTC, ETH, USDT, BNB and SOL:\n")

for x in coins:
    print(x['symbol'], x['quote']['EUR']['price'])