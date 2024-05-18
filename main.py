import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a8b42ad213029851c819cd31181800e9'
HEADER = {'Content-type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "generate",
    "photo": "generate"
}

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

body_rename = {
    "pokemon_id": "27766",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/1004.png"
}

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

body_catch = {
    "pokemon_id": "27766"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)