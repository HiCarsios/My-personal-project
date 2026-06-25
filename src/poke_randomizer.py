import random 
import csv
import json
import os
from pathlib import Path 

def load_pokemon(filename, game = None, repeat=True):
    pokemon_data = {}
    seen_names = set()
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Name"]
            is_available = game is None or row.get(game) == "t"
            if not repeat and name in seen_names:
                continue
            if is_available:
                form = row["Form"]
                if form:
                    formname = f"{name}, {form}"
                    pokemon_data[formname] = row
                else:
                    pokemon_data[name] = row
                seen_names.add(name)
    return pokemon_data

def build_pokedex(game = None, repeat = True):
    current_dir = Path(__file__).parent
    data_path = current_dir.parent /"data" / "pokemon_avail.csv"

    if game is None:
        pokedex = load_pokemon(data_path, repeat = repeat)
    elif game == "ScarVi":
        pokedex = load_pokemon(data_path, "ScarVi", repeat)
    elif game == "SwoSh":
        pokedex = load_pokemon(data_path, "SwoSh", repeat)
    else:
        print("this feature has not been implimented, or the game does not exist")
    return pokedex

def random_poke(dex):
    pokemon = random.choice(list(dex))
    return pokemon

def convert_poke_data(poke):
    #poke = pokedex[pokemon]
    poke['HP'] = int(poke['HP'])
    poke['Attack'] = int(poke['Attack'])
    poke['Defense'] = int(poke['Defense'])
    poke['Sp.Attack'] = int(poke['Sp.Attack'])
    poke['Sp.Defense'] = int(poke['Sp.Defense'])
    poke['Speed'] = int(poke['Sp.Defense'])
    poke['BST'] = int(poke['BST'])
    Scarvi = poke.pop("ScarVi")
    Swosh = poke.pop("SwoSh")
    if not poke['Form']:
        Form = poke.pop('Form')
    if not poke['Type 2']:
        Type = poke.pop("Type 2")
    return poke

def change_poke_data(poke, stats = False, types = False, abilities = False):
    #poke must have gone through the convert_poke_data function first
    if stats:
        poke['HP'] = stats[0]
        poke['Attack'] = stats[1]
        poke['Defense'] = stats[2]
        poke['Sp.Attack'] = stats[3]
        poke['Sp.Defense'] = stats[4]
        poke['Speed'] = stats[5]
        poke['BST'] = sum(stats)
    if types:
        poke['Type 1'] = types[0]
        if len(types) > 1:
            poke['Type 2'] = types[1]
        if len(types) == 1 and 'Type 2' in poke:
            Type = poke.pop('Type 2')
    if abilities:
        for i in range(len(abilities)):
            abilityNo = f"Ability {i+1}"
            poke[abilityNo] = abilities[i]
    return poke


def save_pokedex(pokedex):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    filepath = os.path.join(project_root, "data", "custom_pokedex")
    with open(filepath, "w") as f:
        json.dump(pokemon_dict, f, indent=4)
    print(f"Data successfully saved to data folder")