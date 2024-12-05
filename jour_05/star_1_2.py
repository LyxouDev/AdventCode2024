
#####################################
# Première/Deuxième Etoile - Jour 5 #
#####################################
        
from functools import cmp_to_key

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    regles, pages = input_file.read().split('\n\n')

# Créer une fonction clé de comparaison avec les regles récupérées
cmp = cmp_to_key(lambda x, y: -(x+'|'+y in regles))

# Tableau contenant les résultats des 2 défis ([0]-> défi 1, [1]-> défi 2)
result = [0, 0]
for page in pages.split():
    page = page.split(',')
    s = sorted(page, key=cmp)
    result[page!=s] += int(s[len(s)//2])

print(*result)
