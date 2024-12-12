
######################################
# Première/Deuxième Etoile - Jour 11 #
######################################
        
#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = list(map(int, input_file.readline().strip().split()))

memory = {}

def solve(input, blinks):
    if blinks == 0:
        return 1
    elif (input, blinks) in memory:
        return memory[(input, blinks)]
    elif input == 0:
        val = solve(1, blinks - 1)
    elif len(str_stone := str(input)) % 2 == 0:
        mid = len(str_stone) // 2
        val = solve(int(str_stone[:mid]), blinks - 1) + solve(int(str_stone[mid:]), blinks - 1)
    else:
        val = solve(input * 2024, blinks - 1)
    memory[(input, blinks)] = val
    return val

print(sum(solve(input, 25) for input in inputs))
print(sum(solve(input, 75) for input in inputs))
