from bs4 import BeautifulSoup
import requests
from csv import writer

for pno in range(1,25):
    url="https://www.pararius.com/apartments/amsterdam/page-"+str(pno)
    page = requests.get(url)
    # print(page.content)
    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('section',class_="listing-search-item" )
    # print(lists)
    
with open(r"C:\Python\PY DS\housing_webscraping_all.csv",'a',newline='') as f:
    thewriter = writer(f)
    if pno==1:
        header=["Title","Location","Price","Area","Rooms"]
        thewriter.writerow(header)
            
    for l in lists:
        title=l.find("h2", class_="listing-search-item__title").text.replace('\n','')
        location=l.find("div", class_="listing-search-item__sub-title").text.replace('\n','')
        price=l.find("div", class_="listing-search-item__price").text.replace('\n','')
        area= l.find("li", class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n','')
        rooms=l.find("li", class_="illustrated-features__item illustrated-features__item--number-of-rooms").text.replace('\n','')
            
        info=[title,location,price,area,rooms]
        print(info)
        thewriter.writerow(info)