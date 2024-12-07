
############################
# Deuxieme Etoile - Jour 6 #
############################
        
#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.read().split('\n')

    inputs = [[elt for elt in line] for line in inputs]

# Definition du nombre de ligne, colonne de la grille
nb_lines = len(inputs)
nb_cols = len(inputs[0])

# Coordonnées du point de départ
for i in range(nb_lines):
    for j in range(nb_cols):
        if inputs[i][j] == '^':
            start_x, start_y = i, j

# Fonction de vérification de la boucle courante
def verif_boucle():
    x, y = start_x, start_y 
    dx, dy = -1, 0
    visite = set()

    while True:
        if (x, y, dx, dy) in visite:
            return True

        visite.add((x, y, dx, dy))

        if not (0 <= x + dx < nb_lines and 0 <= y + dy < nb_cols):
            return False

        if inputs[x + dx][y + dy] == '#':
            dy, dx = -dx, dy
        else:
            x += dx
            y += dy

result = 0
for line in range(nb_lines):
    for col in range(nb_cols):
        if inputs[line][col] != '.':
            continue
        inputs[line][col] = '#'

        if verif_boucle():
            result += 1
        inputs[line][col] = '.'

print(result)
