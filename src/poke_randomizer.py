import random 
import csv
from pathlib import Path 

def load_pokemon(filename, game == None):
    pokemon_data = {}
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get(game_name) == "t":
                name = row["name"]
                pokemon_data[name] = row
    return pokemon_data

def build_pokedex(game = None):
    current_dir = Path(__file__).parent
    data_path = current_dir.parent /"data" / "pokemon.csv"

    if game is None:
        pokedex = load_pokemon(data_path)
    elif game == "ScarVi":
        pokedex = load_pokemon(data_path, "ScarVi")
    elif game == "SwoSh":
        pokedex = load_pokemon(data_path, "SwoSh")
    else:
        print("this feature has not been implimented, or the game does not exist")
    return pokedex

def random_poke(dex):
