import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a101a92343c0a75cee5086b34cd13d5a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
QUERY = {'trainer_id' : '6167'}

response_get = requests.get(url = f'{URL}/trainers', params = QUERY)
data = response_get.json()['data'][0]['id']
print(data)
print(response_get.text)