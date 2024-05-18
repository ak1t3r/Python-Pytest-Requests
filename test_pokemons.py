import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a8b42ad213029851c819cd31181800e9'
HEADER = {'Content-type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 3174

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_piece_body():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['trainer_name'] == 'Анастас'