
######################################
# Première/Deuxième Etoile - Jour 10 #
######################################

def dfs(carte, start):
    queue = [start]
    reachable_9s = []

    while queue:
        row, col = queue.pop()
        if carte[row][col] == 9:
            reachable_9s.append((row, col))

        # Vérifie au dessus
        if carte[row - 1][col] == carte[row][col] + 1:
            queue.append((row - 1, col))
        # Vérifie en dessous
        if carte[row + 1][col] == carte[row][col] + 1:
            queue.append((row + 1, col))
        # Vérifie à gauche
        if carte[row][col - 1] == carte[row][col] + 1:
            queue.append((row, col - 1))    
        # vérifie à droite
        if carte[row][col + 1] == carte[row][col] + 1:
            queue.append((row, col + 1))

    return len(set(reachable_9s)), len(reachable_9s)

carte, depart = [], []

with open('input.txt', "rt") as fin:
    for row, line in enumerate(fin):
        carte.append(list(map(int, line.strip())))
        depart.extend((row, col) for col, height in enumerate(carte[-1]) if height == 0)
        carte[-1].append(0)

    carte.append([0] * len(carte[0]))

sum_part1, sum_part2 = 0, 0
for h in depart:
    v1, v2 = dfs(carte, h)
    sum_part1 += v1
    sum_part2 += v2

print(f"Star 1: {sum_part1}")
print(f"Star 2: {sum_part2}")
