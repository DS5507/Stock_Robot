#robo_advisor.py

import csv
import json
import os


from dotenv import load_dotenv
import requests
import datetime


load_dotenv()


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

localtime = '{0:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())

while True:
    symbol = input(str("Please select a stock symbol: ")).upper()
    while len(symbol) >= 6:
        print("Stock symbols should be 5 characters or less")
        break
    else:
        print("Finding Stock Information...")
        break

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_Daily&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
parsed_response = json.loads(response.text) #> type=dict


## TODO: Figure out API Validation

#print(type(response)) #><class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text) #>



last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: Assumes first day is on top.  Sort to ensure latest day is first

latest_day = dates[0] #"2019-02-20"

latest_close = tsd[latest_day]["4. close"] #> 1,000.00


high_prices = []
low_prices = []


for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices) #max of all high prices
recent_low = min(low_prices) # TODO: Confirm low price
    
    

#
# Info Outputs
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })



print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {localtime}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
breakpoint()
if int(latest_day["4. close"]) <= 1.2*int(recent_low):
    print("RECOMMENDATION: BUY!")
else:
    print("Don't Buy")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

