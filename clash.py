
import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# variables loaded in from .env file
COC_TOKEN = os.environ.get("COC_TOKEN")

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer ' + COC_TOKEN
}

def get_user(user_id):
    # return user profile information
    response = requests.get(f'https://api.clashofclans.com/v1/players/%{user_id}', headers=headers)
    user_json = response.json()
    print(user_json['name'])
    
def search_clan(name):
    # submit a clan search
    response = requests.get(f'https://api.clashofclans.com/v1/clans?name={name}', headers=headers)
    clan_json = response.json()
    for clan in clan_json['items']:
        print(clan['name'] + ' is level ' + str(clan['clanLevel']))


get_user('9L9GLQLJ')
search_clan('Raz3 Predators')