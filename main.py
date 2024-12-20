import requests


URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'a101a92343c0a75cee5086b34cd13d5a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}
 # Получаем список живых покемонов
response_get = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id' : '6167', 'status' : '1'})
data = response_get.json()
message = data.get('message')
if message == 'Покемоны не найдены':
    print ('Покемоны не найдены')
else:
    pokemon_id = response_get.json()['data'][0]['id']

    # Создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create.text)

    # Изменение покемона
if message == 'Покемоны не найдены':
    print ('Покемоны не найдены. Изменять некого')    
else:
    pokemon_id = response_get.json()['data'][0]['id']
    response_put = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = 
        {
        "pokemon_id": pokemon_id,
        "name": "New Name",
        "photo_id": 2
        })
    print(response_put.text)

    # Поймать покемона в покебол
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = {"pokemon_id": pokemon_id})
print(response_catch.text)


    # Получить своего живого покемона первого в списке

'''response_get = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id' : '6167', 'status' : '1'})
data = response_get.json()
message = data.get('message')
if message == 'Покемоны не найдены':
    print ('Покемоны не найдены')
else:
    pokemon_id = response_get.json()['data'][0]['id']
    print(f'Первый покемон в списке: {pokemon_id}')
    print(data)'''

    # Отправить покемона в нокаут первого из списка

'''response_get = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id' : '6167', 'status' : '1'})
data = response_get.json()
message = data.get('message')
if message == 'Покемоны не найдены':
    print ('Покемоны не найдены')
else:
    pokemon_id = response_get.json()['data'][0]['id']      
    response_knockout = requests.post(url= f'{URL}/pokemons/knockout', headers= HEADER, json={'pokemon_id': pokemon_id})
    print(response_knockout.text)'''