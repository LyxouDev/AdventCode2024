

############################
# Deuxième Etoile - Jour 3 #
############################

import re

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.readlines()

result=0
# Définition de l'expression régulière de recherche des chaines de caractère : mul(x, y) ou do() ou don't()
regex = r"mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)"

ok = True
for i in range(len(inputs)):
    # Extraction des chaînes recherchées dans chacune des lignes
    matches=re.findall(regex, inputs[i])

    # Parcours des resultats
    for elt in matches: 
        # Action suivant élément courant des résultats
        match elt:
            case "do()":
                ok = True
                
            case "don't()":
                ok = False

            case _:
                # Suppression des caractères 'mul(' et ')' de chaque extraction
                entiers_extraits = [int(elt) for elt in elt.replace('mul(','').replace(')', '').split(',')]
                if ok:
                    result += (entiers_extraits[0] * entiers_extraits[1])

print(result)