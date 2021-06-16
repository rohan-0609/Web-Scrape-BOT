import requests
from bs4 import BeautifulSoup # used to pass or extract that in
import time
import csv

 # url for google stocks, Accenture and microsoft

urls = ["https://finance.yahoo.com/quote/ACN?p=ACN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

csv_file = open("stocks.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Days Range', '52 week Range', 'Volume', 'Avg Volume'])

for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers)  # helps to make all the queries from a particular web page

    soup = BeautifulSoup(html_page.content, 'lxml')  # lxml is a parser used for fetching html web content

    header_info = soup.find_all("div", id="quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    stock_current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()

    stock.append(stock_title)
    stock.append(stock_current_price)

    table_info = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


    for i in range(0, 8):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)

    csv_writer.writerow(stock)
    time.sleep(20) # taking another loop after 20 seconds

