import requests
import csv
from bs4 import BeautifulSoup


url = 'https://www.jumia.co.ke/mlp-top-deals/?source=MSTB_TW24_GEN'
response = requests.get(url)


# print(response.content)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

names=soup.find_all('h3', class_='name')
for name in names:
     print(name.text)
prices=soup.find_all('div', class_='prc')
for price in prices:
     print(price.text, name.text)


with open('names and prices.csv', 'w',newline='')as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['price and names'])
    for price in prices:
         writer.writerow({price.text,name.text})