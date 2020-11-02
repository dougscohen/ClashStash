
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
            
            
        self.heroes_lookup = {}
        for hero in self.heroes:
            self.heroes_lookup[hero['name']] = []
            self.heroes_lookup[hero['name']].append(hero['level'])
            self.heroes_lookup[hero['name']].append(hero['maxLevel'])
            self.heroes_lookup[hero['name']].append(hero['village'])
    
            
    # ideas
    # 1. list achievements
    # 2. "your labels"
    def get_labels(self):
        return [entry['name'] for entry in self.labels]
    # 3. troop, spell, and hero levels
    
    def get_troop_info(self, troop):
        base = self.troops_lookup[troop][2]
        if base == 'home':
            return f"Your {troop} is a home base troop and is level {self.troops_lookup[troop][0]} out of {self.troops_lookup[troop][1]}"
                    
        else:
            return f"Your {troop} is a builder base troop and is level {self.troops_lookup[troop][0]} out of {self.troops_lookup[troop][1]}"
            
    def get_spell_info(self, spell):
        spell = spell + ' Spell'
        return f"Your {spell} is level {self.spells_lookup[spell][0]} out of {self.spells_lookup[spell][1]}"

    def get_hero_info(self, hero):
        base = self.heroes_lookup[hero][2]
        if base == 'home':
            return f"Your {hero} is from home base and is level {self.heroes_lookup[hero][0]} out of {self.heroes_lookup[hero][1]}"
                    
        else:
            return f"Your {hero} is from builder base and is level {self.heroes_lookup[hero][0]} out of {self.heroes_lookup[hero][1]}"


    # show them how long until heroes are maxed for their TH??




class Clan(object):
    """
    docstring
    """
    def __init__(self, clantag):
        
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%{clantag}', headers=headers)
        clan_dict = response.json()
    
        for key in clan_dict: 
            setattr(self, key, clan_dict[key]) 
        



# def search_clan(name):
#     # submit a clan search
#     response = requests.get(f'https://api.clashofclans.com/v1/clans?name={name}', headers=headers)
#     clan_json = response.json()
#     for clan in clan_json['items']:
#         print(clan['name'] + ' is level ' + str(clan['clanLevel']))

player = Player('LJ82PUCCG')
clan = Clan('9YOLVRVO')
print(clan.warLeague)

# search_clan('Raz3 Predators')


# Viz ideas


# down the road ideas with ML
# 1. recommend clans to join (clans that have people like you)
# 2. recommend who in your clan to friendly challenge
# 3. predict how long until you max your TH?
# 4. predict which clan will win the war