
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


class Player(object):
    """
    docstring
    """
    def __init__(self, user_id):
        
        response = requests.get(f'https://api.clashofclans.com/v1/players/%{user_id}', headers=headers)
        player_dict = response.json()
    
        for key in player_dict: 
            setattr(self, key, player_dict[key]) 
            
    # ideas
    # 1. list achievements
    # 2. "your labels"
    def get_labels(self):
        return [entry['name'] for entry in self.labels]
    # 3. troop & spell levels
    def troops_overview(self):
        self.troops_dict = {}
        for troop in self.troops:
            self.troops_dict[troop['name']] = []
            self.troops_dict[troop['name']].append(troop['level'])
            self.troops_dict[troop['name']].append(troop['maxLevel'])
            self.troops_dict[troop['name']].append(troop['village'])
            
        return self.troops_dict
            

# def get_user_name(user_id):
#     # return user profile information
#     response = requests.get(f'https://api.clashofclans.com/v1/players/%{user_id}', headers=headers)
#     user_json = response.json()
#     print(user_json['name'])
    
# def search_clan(name):
#     # submit a clan search
#     response = requests.get(f'https://api.clashofclans.com/v1/clans?name={name}', headers=headers)
#     clan_json = response.json()
#     for clan in clan_json['items']:
#         print(clan['name'] + ' is level ' + str(clan['clanLevel']))

player = Player('9L9GLQLJ')
print(player.troops_overview())

# search_clan('Raz3 Predators')