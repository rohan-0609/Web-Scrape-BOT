# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests  # used to obtain the html information from web page
from bs4 import BeautifulSoup # used to pass or extract that in
import time

 # url for google stocks, Accenture and microsoft
urls = ["https://finance.yahoo.com/quote/ACN?p=ACN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

for url in urls:
    html_page = requests.get(url, headers=headers)  # helps to make all the queries from a particular web page

    soup = BeautifulSoup(html_page.content, 'lxml')  # lxml is a parser used for fetching html web content

    header_info = soup.find_all("div", id="quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    stock_current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()
    # print("Current Goggle Stock price is: $", stock_current_price)
    print("Current stock is: $", stock_current_price)

    table_info = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")
    # comes under tr tag
    print("=============")
    stock_title = soup.find("h1").get_text()
    print("COMPANY :", stock_title)
    print("============")


    for i in range(0, 8):
        heading = table_info[i].find_all("td")[0].get_text()
        value = table_info[i].find_all("td")[1].get_text()
        print(heading, ": $", value)

    time.sleep(5)

