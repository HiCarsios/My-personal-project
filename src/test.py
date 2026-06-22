from stat_randomize import *
from poke_randomizer import *
from type_randomizer import *
from ability_randomizer import *

def poke_exists():
    pokeone = balanced_stats()
    print(pokeone)
    return

def test_balance():
    balance_value = 0
    extremes = 0
    extremel =0
    good = 0
    #when testing I upped the range to 100 000 but was lowered to ease future tests
    for i in range(10):
        check = balanced_stats()
        checksum = sum(check)
        if checksum >=400 and checksum <=700:
            balance_value += 1
        for f in check:
            if f <20:
                extremes += 1
            elif f > 180:
                extremel +=1
            elif f >60 and f < 120:
                good +=1
    return {"balance": balance_value, "extreme smalls": extremes, "extreme large": extremel, "good": good}

def test_equal(total = 555):
    extreme = 0
    breaking = 0
    #again I tested with 100 000 however I lowered for future tests
    for i in range(10):
        poke = equal_random(total)
        for f in poke:
            if f >255:
                breaking +=1
            elif f >230:
                extreme +=1
    return{"with total": total, "game breakers":breaking, "extremes":extreme}

def basic_randomizer():
    pokeone = balanced_stats()
    poketwo = balanced_stats()
    pokethree= balanced_stats()
    view_stats(pokeone)
    view_stats(poketwo)
    view_stats(pokethree)


def main():
    #poke_exists()
    #balanced = test_balance()
    #print(balanced)
    #legend = test_equal(680)
    #arceus = test_equal(720)
    #azuril = test_equal(180)
    #arcanine = test_equal()
    #print(legend)
    #print(arceus)
    #print(azuril)
    #print (arcanine)
    nationaldex = build_pokedex()
    Scarletdex = build_pokedex("ScarVi")
    Sworddex = build_pokedex("SwoSh", repeat = False)
    #print(nationaldex)
    #print(Scarletdex)
    #print(Sworddex)
    #These above lines are commented out to not distract you with a giant wall of text
    national_poke = random_poke(nationaldex)
    scarvi_poke = random_poke(Scarletdex)
    Swo_poke = random_poke(Sworddex)
    print(national_poke, scarvi_poke, Swo_poke)
    print(Scarletdex[scarvi_poke])
    step_poke = convert_poke_data(nationaldex[national_poke])
    scarv_poke = convert_poke_data(Scarletdex[scarvi_poke])
    print(step_poke)
    #shuf = shuffle_stats(step_poke)
    #print(shuf)
    types = rand_type(True)
    typestwo = rand_type(True, True)
    print(types, typestwo)
    statchange = balanced_stats()
    step_poke = change_poke_data(step_poke, types = types)
    scarv_poke = change_poke_data(scarv_poke, stats = statchange, types = typestwo)
    #print(step_poke)
    print(scarv_poke)
    every_abilty = build_ability_list()
    twf_abilities = build_ability_list(cringe = True, double = True, unavail = True, nega = True)
    starter_ables = random_ability(every_abilty, 3)
    print(starter_ables)
    scarv_poke = change_poke_data(scarv_poke, abilities = starter_ables)
    print(scarv_poke)

main()