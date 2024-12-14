
######################################
# Première/Deuxième Etoile - Jour 14 #
######################################

import re

# Définition des dimensions de la grille
w, h = 101, 103

# Récupération de la position de chacun des robots et de leurs déplacements
bots = [[*map(int, re.findall(r'-?\d+',l))] for l in open('input.txt')]

def danger(t):
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * t) % w
        y = (y + dy * t) % h

        a += x > w//2 and y > h//2
        b += x > w//2 and y < h//2
        c += x < w//2 and y > h//2
        d += x < w//2 and y < h//2

    return a * b * c * d

# Affichage des résultats de la partie 1 et 2
print(danger(100))
print(min(range(10_000), key=danger))
