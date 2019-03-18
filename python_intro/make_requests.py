import requests
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

"""Getting data for DAX-30"""
r = requests.get("http://en.boerse-frankfurt.de/index/DAX")
soup = BeautifulSoup(r.content, 'html.parser')
print(locale.atof(soup.find(attrs={"source": 'lightstreamer', 'field': 'last'}).text))

"""Getting data for Dow Jones"""
r = requests.get("https://www.marketwatch.com/investing/index/djia")
# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
print(locale.atof(soup.find('div', class_='intraday__data').find('h3', class_='intraday__price').text))
