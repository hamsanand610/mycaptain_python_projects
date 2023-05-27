import requests
from bs4 import BeautifulSoup
import csv

url ="'https://www.nytimes.com/books/best-sellers/hardcover-fiction/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data = []
for item in soup.find_all('div', class_='item'):
    title = item.find('h2').text.strip()
    description = item.find('p').text.strip()
    price = item.find('span', class_='price').text.strip()
    data.append([title, description, price])
    
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description', 'Price'])
    for row in data:
        writer.writerow(row)