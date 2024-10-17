from bs4 import BeautifulSoup
import requests
import json
games = {}
session = requests.Session()
url = 'https://www.igromania.ru/games/pc/all/'
html = session.get(url, timeout=5)
soup = BeautifulSoup(html.text, 'html.parser')

for page in soup.find_all(class_='GameCard_root__hTtZo'):
    name = page.find(class_='GameCard_title__RBpyU')
    ganre = page.find(class_='GameCard_genres__xIhJz')
    games['name'] = name.text
    games['ganre'] = ganre.text.split(',')
    json_str = json.dumps(games, ensure_ascii=False)
    with open('games.json', 'a', encoding='utf-8') as file:
        file.write(json_str)
        file.write(',')
