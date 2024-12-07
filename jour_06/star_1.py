
############################
# Première Etoile - Jour 6 #
############################
        
#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.read().split('\n')

# Definition du nombre de ligne, colonne de la grille
nb_lines = len(inputs)
nb_cols = len(inputs[0])

# Coordonnées du point de départ
for i in range(nb_lines):
    for j in range(nb_cols):
        if inputs[i][j] == '^':
            x, y = i, j

dx, dy = -1, 0
visite = set()

while True:
    visite.add((x, y))

    if not (0 <= x + dx < nb_lines and 0 <= y + dy < nb_cols):
        break
    if inputs[x + dx][y + dy] == '#':
        dy, dx = -dx, dy
    else:
        x += dx
        y += dy

print(len(visite))
