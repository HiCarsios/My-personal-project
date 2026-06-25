from stat_randomize import *
from poke_randomizer import *
from type_randomizer import *
from ability_randomizer import *
import sys

def main():
    print("A Pokemon Randomizer by Carsios")
    print("1: Pokemon")
    print("2: Stats")
    print("3: Abilities")
    print("4: Types")
    choice = input("Please select everything you want to generate about a Pokemon. ")
    game = None
    frozen_stats = None
    if '1' in choice:
        repeat = True
        repeat_random = False
        print("---Let's Pick a Pokemon---")
        print("1. Any, 2. Scarlet & Violet 3. Sword & Shield")
        games = input("Which game is it from? ")
        print("Yes or No")
        forms = input("Do you want to see repeat forms? ")
        repeat_pokemon= input("Do you want to see Pokemon multiple times? ")
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
        print("---Let's make some stats---")
        print("1:Fully random")
        print("2:Balanced random(Pokemon will usually have 450-650 stats)")
        print("3:All the same BST")
        print("4:What the original Pokemon is")
        print("5:Shuffle the orignal Pokemon's Stats")
        stat_choice = input("How do you want your Pokemon's stats to be? ")
        if "1" in stat_choice:
            statfunction = pure_random
        elif "2" in stat_choice:
            statfunction = balanced_stats
        elif "3" in stat_choice:
            statfunction = equal_random
            frozen_stats = input("What do your Pokemon's Base stat total to be? ")
            frozen_stats = int(frozen_stats)
        elif "4" in stat_choice:
            statfunction = equal_random
        elif "5" in stat_choice:
            if '1' not in choice:
                sys.exit("Error: Pokemon must be generated for shuffle")
            statfunction = shuffle_stats
            shuffle = True

    if '3' in choice:
        cringe = False
        double = False
        unavail = False
        nega = False
        scarv = False
        rmv_abl =False
        print("---Let's generate some abilities---")
        print("1. Ban overpowered abilities")
        print("2. Ban doubles-only abilities")
        print("3. Ban Negative abilities")
        print("4. Ban Pokemon-specifc abilities")
        if '1' not in choice:
            print("5: Ban abilities not in Sword & Shield")
        ability_choice = input("Which abilities to you want to randomize from? ")
        no_of_abilities = input("How many abilities should this pokemon have? ")
        no_of_abilities = int(no_of_abilities)
        print("Yes/No")
        remove_abilities = input("Would you like to remove abilities after you see them? ")
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
        if "yes" in remove_abilities.lower():
            rmv_abl = True
        ability_list = build_ability_list(cringe, double, unavail, nega, scarv)

    if '4' in choice:
        same_type = False
        weighted = False
        print("---Let's generate some types---")
        print("Yes/No")
        roundtype = input("Do you want the same type every round? ")
        weight = input("Do you want types to be weighted based on how popular they are? ")
        print("Single, Dual or, Random (pick only one)")
        nooftypes = input("Do you want to see only Single or Dual type Pokemon? ")
        if "yes" in weight.lower():
            weighted = True
        if "yes" in roundtype.lower():
            same_type = True

    while True:
        Lookup = input("---Would you like to generate round by round (rr) or Lookup (l)")
        if 'rr' in Lookup:
            roundsize = input("How many Pokemon should we generate each time? ")
            roundsize = int(roundsize)
            Everyone = []
            rr = True
            look = False
            break
        elif 'l' in Lookup and '1' not in choice:
            print("Cannot do lookup without creating pokedex, please select 1 at the start along with any other choices")
        elif 'l' in Lookup:
            look = True
            rr = False
            generated = False
            break
        else:
            print("Please put in either 'rr' or 'l'")


    while rr == True:
        Pokemon = []
        if '1' in choice:
            for i in range(roundsize):
                Pokename = random_poke(pokedex)
                Poke = pokedex[Pokename]
                Poke = convert_poke_data(Poke)
                if repeat_random:
                    del pokedex[Pokename]
                Pokemon.append(Poke)
        else:
            #I need to create spots for the future data to go if no pokemon are generated
            for i in range(roundsize):
                Poke = {}
                Pokemon.append(Poke)
        if '2' in choice:
            for l in range(len(Pokemon)):
                if shuffle:
                    Pokemon[l] = shuffle_stats(Pokemon[l])
                    continue
                if frozen_stats:
                    stats = statfunction(frozen_stats)
                else:
                    stats = statfunction(Pokemon[l]['BST'])
                Pokemon[l] = change_poke_data(Pokemon[l], stats = stats)
        if '3' in choice:
            for l in range(len(Pokemon)):
                abilities = random_ability(ability_list, no_of_abilities)
                Pokemon[l] = change_poke_data(Pokemon[l], abilities = abilities)
                if rmv_abl:
                    ability_list = remove_repeats(ability_list, abilities)
        if '4' in choice:
            seen_type = False
            for l in range(len(Pokemon)):
                if '1' in nooftypes or 'single' in nooftypes.lower():
                    types = 1
                elif '2' in nooftypes or 'dual' in nooftypes.lower():
                    types = 2
                else:
                    types = one_or_two()
                if seen_type or not same_type:
                    type_for_pokemon = rand_type(types, weighted)
                Pokemon[l] = change_poke_data(Pokemon[l], types = type_for_pokemon)
        Everyone.append(Pokemon)
        print(Pokemon)
        breaker = input("Would you like to continue? (Yes or No) ")
        if "yes" in breaker.lower():
            continue
        break



    while look == True:
        if not generated:
            for p in list(pokedex):
                pokedex[p]= convert_poke_data(pokedex[p])
                if '2' in choice:
                    if shuffle:
                        pokedex[p] = shuffle_stats(pokedex[p])
                        continue
                    if frozen_stats:
                        stats = statfunction(frozen_stats)
                    else:
                        stats = statfunction(pokedex[p]['BST'])
                    pokedex[p]= change_poke_data(pokedex[p], stats = stats)
                if '3' in choice:
                    abilities = random_ability(ability_list, no_of_abilities)
                    pokedex[p] = change_poke_data(pokedex[p], abilities = abilities)
                if '4' in choice:
                    if '1' in nooftypes or 'single' in nooftypes.lower():
                        types = 1
                    elif '2' in nooftypes or 'dual' in nooftypes.lower():
                        types = 2
                    else:
                        types = one_or_two()
                    type_for_pokemon = rand_type(types, weighted)
                    pokedex[p] = change_poke_data(pokedex[p], types = type_for_pokemon)
            generated = True
            print("---Pokedex Randomized---")
            print("REMINDER! Names are case and punctuation sensitive")
        Pokefind = input("Which Pokemon do you want to find? ")
        Export_list = input("Would you like to save this list of pokemon to data? ")
        if Pokefind in pokedex:
            print(pokedex[Pokefind])
        else:
            print("ERROR: Pokemon not found")
        cont = input("Would you like to continue? (yes or no or new pokemon) ")
        if 'yes' in cont.lower() or '1' in cont or cont in pokedex:
            if cont in pokedex
            print(pokedex[cont])
            continue
        Export_list = input("Would you like to save this list of pokemon to data? ")
        if "yes" in Export_list.lower():
            are_you_sure = input("Are you sure you want to save, this will overwrite any previous data")
            if "yes" in are_you_sure:
                save_pokedex(pokedex)
        break


if __name__ == "__main__":
    main()