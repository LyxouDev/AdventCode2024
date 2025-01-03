
############################
# Première Etoile - Jour 4 #
############################
        
import numpy as np

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.read().split('\n')

rows = len(inputs)
cols = len(inputs[0])
search_grid = np.ndarray((rows, cols), dtype=int)
for i, L in enumerate(inputs):
    for j, c in enumerate(L):
        search_grid[i,j] = ord(c)

total = 0
for i in range(rows):
    for j in range(cols):
        if search_grid[i,j] == ord('X'):
            directions = [(a,b) for a in [-1, 0, 1] for b in [-1, 0, 1]]
            for d in directions:
                xmas_flag = True
                for k, c in enumerate(['M', 'A', 'S'], start=1):
                    if i + k * d[0] < 0 or i + k * d[0] >= rows \
                        or j + k * d[1] < 0 or j + k * d[1] >= cols \
                            or search_grid[i + k * d[0], j + k * d[1]] != ord(c):
                        xmas_flag = False
                        break
                if xmas_flag:
                    total += 1
print(total)
