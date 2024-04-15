import requests
import csv
from bs4 import BeautifulSoup

def url_input(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    names = soup.find_all('h3', class_='name')
    prices = soup.find_all('div', class_='prc')

    with open('names_and_prices.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Price'])
        for name, price in zip(names, prices):
            writer.writerow([name.text.strip(), price.text.strip()])

url_input(url='https://www.jumia.co.ke/')