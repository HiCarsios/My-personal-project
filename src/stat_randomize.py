import random


def balanced_stats(stats = None):
    base_stat =[]
    for i in range(6):
        x = random.randint(0,10)
        y = random.randint(1,10)
        z = random.randint(0,10)
        stat = x **2 + 10*y + z
        base_stat.append(stat)
    return base_stat

def pure_random(stats = None):
    base_stat = []
    for i in range(6):
        stat = random.randint(10,230)
        base_stat.append(stat)
    return base_stat

def equal_helper(bst, i):
    avg_remain = bst // (5-i)
    x = random.randint(-10,10)
    y = random.randint(0,6)
    z = random.randint(-3,3)
    stat = avg_remain + y**2 + x + 10*z
    proper_remains = bst -stat - ((6-i) * 10)
    if stat < 0 or proper_remains < 0 or stat >250:
        stat = equal_helper(bst,i)
    return stat

def equal_random(value = 555):
    base_total = value
    base_stats = []
    for i in range(5):
        stat = equal_helper(base_total, i)
        base_total = base_total - stat
        base_stats.append(stat)
    base_stats.append(base_total)
    random.shuffle(base_stats)
    return base_stats


def view_stats(stats):
    bst =  sum(stats)
    sight = {"bst":bst, "HP":stats[0], "ATK":stats[1], "DEF":stats[2], "SPA":stats[3], "SPD":stats[4], "SPE":stats[5]}
    print(sight)
    return

def shuffle_stats(poke):
    #data must have gone through convert poke already
    pokestats = [poke['HP'], poke['Attack'], poke['Defense'], 
    poke['Sp.Attack'], poke['Sp.Defense'], poke['Speed']]
    random.shuffle(pokestats)
    poke['HP'] = pokestats[0]
    poke['Attack'] = pokestats[1]
    poke['Defense'] = pokestats[2]
    poke['Sp.Attack'] = pokestats[3]
    poke['Sp.Defense'] = pokestats[4]
    poke['Speed'] = pokestats[5]
    return poke