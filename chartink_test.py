import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489} ( {cash} ( [0] 15 minute supertrend( 10,3 ) < latest close and [ -1 ] 15 minute supertrend( 10,3 ) >= 1 day ago  close and [0] 15 minute supertrend( 14,3 ) < latest close and [ -1 ] 15 minute supertrend( 14,3 ) >= 1 day ago  close and [0] 15 minute supertrend( 9,2 ) < latest close and [ -1 ] 15 minute supertrend( 9,2 ) >= 1 day ago  close and [0] 15 minute close > 1 day ago high )  ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)


#{"scan_clause" : " "}
