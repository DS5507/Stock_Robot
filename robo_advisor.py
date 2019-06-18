#robo_advisor.py

import csv
import json

import requests


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo"

response = requests.get(request_url)
#print(type(response)) #><class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text) #>
 
  
parsed_response = json.loads(response.text) #> type=dict

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: Assumes first day is on top.  Sort to ensure latest day is first

latest_day = dates[0] #"2019-02-20"

latest_close = tsd[latest day]["4. close"] #> 1,000.00


high_prices = []
low_prices[]


for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices) #max of all high prices
recent_low = min(low_prices)
    
    

#
# Info Outputs
#

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("WRITING DATA TO CSV...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


csv_file_path = "XX.csv"

with open(csv_file_path, "w") as csv_file
    writer = csv.DictWriter(csv_file, fieldnames=[" "], [" "])
    writer.writeheader()
    writer.writerow


