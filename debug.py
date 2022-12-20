import requests
from bs4 import BeautifulSoup

url = 'https://elmir.ua/configurator/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
find_text = soup.find('div', {'class': 'prodgrp'}).get_text()

#
# from lxml import html
#
# tree = html.fromstring('<содержимое какой-то страницы>')
#
# tree.xpath('.//div[@id="<какой-то определенный id>"]')[0].text