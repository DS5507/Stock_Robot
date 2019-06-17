## robo_advisor.py

import requests
import json



request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo"

response = request.get(request_url)
#print(type(response)) #><class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text) #>
 
  
parsed_response = json.loads(response.text) #> type=dict

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]




#
# Info Outputs
#

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: "{last_refreshed})
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")