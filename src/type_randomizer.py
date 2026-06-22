import random

types = ["Rock", "Water", "Electric", "Grass", "Poison", "Psychic",
"Fire", "Ground", "Flying", "Bug", "Normal", "Ghost", "Fighting",
"Steel", "Ice", "Dragon", "Fairy", "Dark"]

def rand_type(Dualtype, weighted = False):
    typeno = 1
    if Dualtype:
        typeno = 2
    if weighted:
        choice = random.choices(types, weights =[80, 162, 75, 133, 89,111, 90, 79, 115, 94, 134, 76, 86, 81, 60, 78, 72, 84], k = typeno)
    else:
        choice = random.sample(types, k =typeno)
    return choice

