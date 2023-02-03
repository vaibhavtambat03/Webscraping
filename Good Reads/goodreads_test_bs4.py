import pandas as pd
import lxml
import requests
from bs4 import BeautifulSoup
url=requests.get("https://www.goodreads.com/quotes/tag/authors")
content=url.content
print(content)

soup=BeautifulSoup(content,"lxml")

a=[]
author_name=soup.find_all("span",class_="authorOrTitle")
for i in author_name:
    a.append(i.text.strip())
print(a)

b=[]
quote=soup.find_all("div",class_="quoteText")
for i in quote:
    i=i.text.replace('\n','')
    i=i.strip()
    b.append(i)
print(b)

c=[]
tags=soup.find_all("div",class_="greyText")
for i in tags:
    i=i.text.strip()
    i=i.replace('\n','')
    i=i.replace('tags:','')
    i=i.replace(' ','')
    c.append(i)
print(c)

d=[]
likes=soup.find_all("a",class_="smallText")
for i in likes:
    i=i.text.strip()
    i=int(i.replace(" likes",""))
    d.append(i)
print(d)

A=pd.DataFrame(a,columns=["Author_name"])
B=pd.DataFrame(b,columns=["Quote"])
C=pd.DataFrame(c,columns=["Tags"])
D=pd.DataFrame(d,columns=["Likes"])

combined=pd.concat([A,B,C,D],axis=1)
print(combined)
combined.to_csv("C:\Python\PY DS\Webscrapping\goodreads_test_bs4.csv")


