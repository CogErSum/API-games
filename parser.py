import json
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


games = {}
driver = webdriver.Firefox()
def main_loop(page):
    url = f'https://www.igromania.ru/games/pc/all/?page={page}'
    site = driver.get(url)

    for page in driver.find_elements(by=By.CLASS_NAME, value='GameCard_root__hTtZo'):
        name = page.find_element(by=By.CLASS_NAME, value='GameCard_title__RBpyU')
        ganre = page.find_element(by=By.CLASS_NAME, value='GameCard_genres__xIhJz')
        games['name'] = name.text
        games['ganre'] = list(map(lambda s: s.replace('\n', ''), ganre.text.split(',')))
        
        
        print(games)
        json_str = json.dumps(games, ensure_ascii=False)
        with open('games.json', 'a', encoding='utf-8') as file:
            file.write(json_str)
            file.write(',\n')

x = 1
while x !=20:
    main_loop(x)
    x += 1