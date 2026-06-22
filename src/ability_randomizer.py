import random 
import csv
from pathlib import Path 

def build_ability_list(cringe = False, double = False, unavail = False, nega = False, scarv = False):
    current_dir = Path(__file__).parent
    filename = current_dir.parent /"data" / "abilities.csv"
    ability_list = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if cringe and row.get('Cringe') == 't':
                continue
            elif double and row.get('Doubles') == 't':
                continue
            elif unavail and row.get('Unavailable') == 't':
                continue
            elif nega and row.get('Negative') == 't':
                continue
            elif scarv and row.get('ScarVi') == 't':
                continue
            name = row["Name"]
            ability_list.append(name)
    return ability_list

def random_ability(abilities, k = 1):
    ables = random.sample(abilities, k = k)
    return ables
    
def remove_repeats(abilities, ables):
    #abilities is the full list, ables is the previously used abilities
    for a in ables:
        abilities.remove(a)
    return abilities