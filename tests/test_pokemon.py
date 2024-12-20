import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a101a92343c0a75cee5086b34cd13d5a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
QUERY = {'trainer_id' : '6167'}

def test_status_code(): #проверяем, что приходит статус 200
    response_get = requests.get(url = f'{URL}/trainers', params = QUERY)
    assert response_get.status_code == 200
#data = response_get.json()['data'][0]['id']
#print(data)

def test_trainer_name(): # проверяем, что приходит имя тренера
    response_get = requests.get(url = f'{URL}/trainers', params = QUERY)
    assert response_get.json()['data'][0]['trainer_name'] == 'Булат'


    # объединяем два предыдущих теста
@pytest.mark.parametrize('key, value',[('id','6167'),('trainer_name', 'Булат')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = QUERY)
    assert response_parametrize.json()['data'][0][key] == value