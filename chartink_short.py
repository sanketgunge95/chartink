import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489} ( latest close < 1 day ago min( 5 , latest low ) and 1 day ago  close >= 2 day ago  min( 5 , latest low ) ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489} ( 1 day ago high > 2 days ago high and latest high < 1 day ago high and 1 day ago close < 2 days ago high and 1 day ago volume > 3 days ago volume ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('No Loss')
    print(stock_list)
    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {cash} ( latest close < 1 day ago close * 0.97 and latest volume > 100000 and latest volume * latest close > 1000000 and latest close > 8 and latest volume > latest sma( volume,10 ) * 0.75) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('Intraday Buy at 9:30')
    print(stock_list)
  
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489} ( 1 day ago high > 2 days ago high and latest close < 1 day ago high and latest volume > 3 days ago volume and latest high < 1 day ago high ) )"}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('Top 100 intraday task ')
    print(stock_list)  
    

    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {cash}  (( latest low - latest high ) < ( 1 day ago low - 1 day ago high ) and( latest low - latest high ) < ( 2 days ago low - 2 days ago high ) and( latest low - latest high ) < ( 3 days ago low - 3 days ago high ) and( latest low - latest high ) < ( 4 days ago low - 4 days ago high ) and( latest low - latest high ) < ( 5 days ago low - 5 days ago high ) and( latest low - latest high ) < ( 6 days ago low - 6 days ago high ) and( latest low - latest high ) < ( 7 days ago low - 7 days ago high ) and latest close < latest open and latest close < 1 day ago close and weekly close < weekly open and monthly close < monthly open and 1 day ago volume > 10000 and latest sma( close,20 ) < latest sma( close,40 ) and latest sma( close,40 ) < latest sma( close,60 ) and( latest volume ) > ( 1 day ago volume ) * 1.25  ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)
    

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33492}  ( [0] 5 minute close > latest low and [0] 5 minute close < ( ( 1 day ago high + 1 day ago low + 1 day ago close ) / 3 ) and latest volume >= 300000 and latest close > 1000) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)
    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489}  ( [0] 5 minute close < [0] 5 minute ema( close,8 ) and [0] 5 minute close < [0] 5 minute ema( close,34 ) and [0] 5 minute close < [0] 5 minute ema( close,100 ) and [0] 5 minute volume > [0] 5 minute wma( volume,5 ) and [0] 10 minute adx di negative( 14 ) >= 35 and [0] 5 minute ema( close,8 ) < [0] 5 minute ema( close,34 ) and [0] 5 minute ema( close,34 ) < [0] 5 minute ema( close,100 ) ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)
    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489}  ( 1 day ago high > 2 days ago high and latest high < 1 day ago high and 1 day ago close < 2 days ago high and 1 day ago volume > 3 days ago volume ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)
    
    

