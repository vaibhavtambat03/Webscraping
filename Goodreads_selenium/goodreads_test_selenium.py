from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://www.goodreads.com/quotes/tag/authors"
driver.get(url)

author=driver.find_elements(By.XPATH,'//span[@class="authorOrTitle"]')
a=[]
for i in author:
    i=i.text.strip()
    i=i.replace(",","")
    a.append(i)
print(a)
A=pd.DataFrame(a,columns=["Author_name"])

quote=driver.find_elements(By.XPATH,'//div[@class="quoteText"]')
b=[]
for i in quote:
    i=i.text.strip()
    i=i.replace('\n','')
    i=i.replace('“','')
    i=i.replace('”','')
    b.append((i.split("―"))[0])
print(b)
B=pd.DataFrame(b,columns=["Quotes"])

tags=driver.find_elements(By.XPATH,'//div[@class="greyText smallText left"]')
c=[]
for i in tags:
    i=i.text.strip()
    i=i.replace('\n','')
    i=i.replace('tags:','')
    i=i.replace(' ','')
    c.append(i)
print(c)
C=pd.DataFrame(c,columns=["Tags"])

likes=driver.find_elements(By.XPATH,'//a[@class="smallText"]')
d=[]
for i in likes:
    i=i.text.strip()
    i=i.replace(" likes", "")
    i=int(i)
    d.append(i)
print(d)
D=pd.DataFrame(d,columns=["Likes"])

combined=pd.concat([A,B,C,D],axis=1)
print(combined)

combined.to_csv("C:\Python\PY DS\Webscrapping\Goodreads\goodreads_test_selenium.csv")