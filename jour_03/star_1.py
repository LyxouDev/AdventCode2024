
############################
# Première Etoile - Jour 3 #
############################

import re

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.readlines()

result = 0
# Définition de l'expression régulière de recherche de la chaine de caractère : mul(x, y)
regex = r"mul\([0-9]*,[0-9]*\)"

for i in range(len(inputs)):
    # Extraction de la chaîne recherchée dans chacune des lignes
    matches = re.findall(regex, inputs[i])

    # Parcours des résultats
    for elt in matches:
        # Suppression des caractères 'mul(' et ')' de chaque extraction
        entiers_extraits = [int(elt) for elt in elt.replace('mul(','').replace(')', '').split(',')]

        result += (entiers_extraits[0] * entiers_extraits[1])

print(result)
