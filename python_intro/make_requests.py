import requests
# requests.get('https://api.github.com')
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOG&interval=5min&apikey=XSDBOB7PE8R8WREA')
print(r.json())