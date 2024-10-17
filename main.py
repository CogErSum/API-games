from util import json_to_dict
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def all_games():
    return json_to_dict('games.json')

