import requests
import pandas as pd
from bs4 import BeautifulSoup


#       FLIPKART IN THE WEBSCRABING ON  IPHONE MOBILES
response=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)
soup=BeautifulSoup(response.content,'html.parser')


#          IPHONE MODEL NAMES ON GETHERING THE WEBSCRABING
names=soup.find_all('div',class_="_4rR01T")
name=[]
for i in names[0:10]:
    ss=i.get_text()
    name.append(ss)
   

#           IPHONE PRICES ON WEBSCRABING
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:10]:
    ss=i.get_text()
    price.append((ss))
    
#        IPHONE RATING ON WEBSCRABING
ratings=soup.find_all('div',class_="_3LWZlK")
rate=[]
for i in ratings[0:10]:
    ss=i.get_text()
    rate.append(ss)

#       IPHONE IMAGES ON WEBSCRABING
images=soup.find_all('img',class_="_396cs4")
image=[]
for i in images[0:10]:
    ss=i['src']
    image.append(ss)


#       IPHONE LINKS ON WEBSCRABING
links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in links[0:10]:
    ss="https://www.flipkart.com"+i['href']
    link.append(ss)


df=pd.DataFrame()       #   ROWS AND COLOUMS CREATING 
df["NAMES"]=name
df["PRICES"]=price
df["RATINGS"]=rate
df["IMAGES"]=image
df["LINKS"]=link
 

df.to_csv("IPHONE_MOBILE.cvs")    #   PANDAS CVS FILE 
print(df)

    