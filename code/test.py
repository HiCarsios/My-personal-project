from stat_randomize import *

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



def main():
    poke_exists()
    balanced = test_balance()
    print(balanced)
    legend = test_equal(680)
    arceus = test_equal(720)
    azuril = test_equal(180)
    arcanine = test_equal()
    print(legend)
    print(arceus)
    print(azuril)
    print (arcanine)

main()