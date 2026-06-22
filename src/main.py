from stat_randomize import *
from poke_randomizer import *
from type_randomizer import *
from ability_randomizer import *

def main():
    print("A Pokemon Randomizer by Carsios")
    print("1: Pokemon")
    print("2: Stats")
    print("3: Abilities")
    print("4: Types")
    choice = input("Please select everything you want to generate about a Pokemon. ")
    game = None
    if '1' in choice:
        repeat = True
        repeat_random = False
        print("Let's Pick a Pokemon")
        print("1. Any, 2. Scarlet & Violet 3. Sword & Shield")
        games = input("Which game is it from? ")
        print("Yes or No")
        forms = input("Do you want to see repeat forms? ")
        repeat_pokemon= input("Do you want to see Pokemon multiple times")
        if "2" in games:
            game = "ScarVi"
        elif "3" in games:
            game = "SwoSh"
        if "no" in forms.lower():
            repeat = False
        if "no" in repeat_pokemon.lower():
            repeat_random = True
        pokedex = build_pokedex(game, repeat)

    if '2' in choice:
        shuffle = False
        frozen_stats = False
        print("Let's make some Stats")
        print("1:Fully random")
        print("2:Balanced random(Pokemon will usually have 450-650 stats)")
        print("3:All the same BST")
        print("4:What the original Pokemon is")
        print("5:Shuffle the orignal Pokemon's Stats")
        stat_choice = input("How do you want your Pokemon's stats to be ")
        if "1" in choice:
            statfunction = pure_random
        elif "2" in choice:
            statfunction = balanced_stats
        elif "3" in choice:
            statfunction = equal_random
            frozen_stats = input("What do your Pokemon's Base stat total to be ")
            int(frozen_stats)
        elif "4" in choice:
            statfunction = equal_random
        elif "5" in choice:
            statfunction = shuffle_stats
            shuffle = True

    if '3' in choice:
        cringe = False
        double = False
        unavail = False
        nega = False
        scarv = False
        print("Let's generate some abilities")
        print("1. Ban overpowered abilities")
        print("2. Ban doubles-only abilities")
        print("3. Ban Negative abilities")
        print("4. Ban Pokemon-specifc abilities")
        if '1' not in choice:
            print("5: Ban abilities not in Sword & Shield")
        ability_choice = input("Which abilities to you want to randomize from? ")
        if "1" in ability_choice:
            cringe = True
        if "2" in ability_choice:
            double = True
        if "3" in ability_choice:
            nega = True
        if "4" in ability_choice:
            unavail= False
        if "5" in ability_choice or game =="SwoSh":
            scarv = True
        ability_list = build_ability_list(cringe, double, unavail, nega, scarv)

    if '4' in choice:
        same_type = False
        print("Let's generate some types")
        print("Yes/No")
        roundtype = input("Do you want the same type every round? ")
        print("Single, Dual or, Random (pick only one)")
        nooftypes = input("Do you want to see only Single or Dual type Pokemon ")
        if "yes" in roundtype.lower():
            same_type = True

    roundsize = input("How many Pokemon should we generate each time ")
    int(roundsize)
    while True:
        break

if __name__ == "__main__":
    main()