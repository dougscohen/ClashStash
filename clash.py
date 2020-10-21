
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
            
        self.troops_lookup = {}
        for troop in self.troops:
            self.troops_lookup[troop['name']] = []
            self.troops_lookup[troop['name']].append(troop['level'])
            self.troops_lookup[troop['name']].append(troop['maxLevel'])
            self.troops_lookup[troop['name']].append(troop['village'])
            
        self.spells_lookup = {}
        for spell in self.spells:
            self.spells_lookup[spell['name']] = []
            self.spells_lookup[spell['name']].append(spell['level'])
            self.spells_lookup[spell['name']].append(spell['maxLevel'])
    
            
    # ideas
    # 1. list achievements
    # 2. "your labels"
    def get_labels(self):
        return [entry['name'] for entry in self.labels]
    # 3. troop & spell levels
    
    def get_troop_info(self, troop):
        base = self.troops_lookup[troop][2]
        if base == 'home':
        
            return f"Your {troop} is a home base troop and is level {self.troops_lookup[troop][0]} out of {self.troops_lookup[troop][1]}"
                    
        else:
            return f"Your {troop} is a builder base troop and is level {self.troops_lookup[troop][0]} out of {self.troops_lookup[troop][1]}"
            
    def get_spell_info(self, spell):
        spell = spell + ' Spell'
        return f"Your {spell} is level {self.spells_lookup[spell][0]} out of {self.spells_lookup[spell][1]}"

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
print(player.get_spell_info('Freeze'))

# search_clan('Raz3 Predators')