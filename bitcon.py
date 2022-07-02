import requests

responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoindata = responce.json()
data = []

for i in bitcoindata:
 data.append(i)

currency = input(str("In pair of which currency you want to check"
                     " the price of the Bitcoin?"
                      "\nEnter the shortname of the currency in capital"
                      "\nEg. EUR (Euro)\n"))

rate = bitcoindata[data[3]][currency]
print("Price of",bitcoindata[data[2]],"in pair of",rate['description'],
          "on\n",bitcoindata[data[0]]['updated'],
          "\nis",rate['rate'],"\n")



