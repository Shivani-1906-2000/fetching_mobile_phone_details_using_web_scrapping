import requests
from bs4 import BeautifulSoup
import pandas as pd
user={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page=requests.get('https://www.flipkart.com/mobile-phones-store',headers=user)
soup=BeautifulSoup(page.content,'html.parser')

#print(soup.prettify())  #will print all the data of the file

#search=soup.find_all(class_="_2QUpwp")
#print(search[0])

names=[]
phone_names=soup.find_all(class_="iUmrbN")
for name in phone_names:
    names.append(name.getText())

offers=[]
phone_discount=soup.find_all(class_="BXlZdc")
for discount in phone_discount:
    offers.append(discount.getText())

prices=[]
phone_price=soup.find_all(class_="_3o3r66")
for price in phone_price:
    prices.append(price.getText())

mobile_details=pd.DataFrame({'phone_names':names,'phone_discount':offers,'phone_price':prices})
print(mobile_details)


mobile_details.to_csv("mobile.csv")
