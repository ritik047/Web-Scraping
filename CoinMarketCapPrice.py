import requests, json

while True:
    print('use ctrl+c or type EXIT to close the script')
    fiat = input("Provide fiat name eg: USDT, BUSD\t\t\t\t")
    symbol = input("Provide crypto symbol eg: BTC, ETH, BNB\t\t\t")
    endpoint = "https://3rdparty-apis.coinmarketcap.com/v1/cryptocurrency/widget?convert={}&symbol={}".format(fiat, symbol)
    response = requests.get(endpoint)

    if response.status_code==200:
        print(json.dumps(json.loads(response.text), indent=4))
    else:
        print("Oop! Something went wrong. Invalid request query input")