import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'

session = requests.Session()

text = session.get(url, timeout=5)
soup = BeautifulSoup(text.text, 'html.parser')
print(soup)
