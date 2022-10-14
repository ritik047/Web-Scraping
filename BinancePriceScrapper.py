import requests, json

BINANCE_ENDPOINT="https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list"

response = requests.get(BINANCE_ENDPOINT)

i=0
if response.status_code==200:
    for asset in json.loads(response.text).get("data"):
        print(i,end=")")
        i=i+1
        print("NAME: {}\nSYMBOL: {}\nPRICE: {}\nTOTAL-SUPPLY: {}\n24HRS-PRICE-CHANGE: {}\n24HRS-PERCENT-CHANGE: {}"
              .format(asset.get("name"), asset.get("symbol"), asset.get("price"), asset.get("totalSupply"), asset.get("dayChange"), asset.get("dayChangeAmount")), end="\n"+"="*100+"\n")

else:
    print("Oop! something went wrong status code: ", response.status_code)
