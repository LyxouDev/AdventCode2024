
############################
# Deusième Etoile - Jour 1 #
############################

# Initialisation de 2 listes
liste_1 = list()
liste_2 = list()

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.readlines()

    for i in range(len(inputs)):
        inputs[i] = inputs[i].split()

        liste_1.append(int(inputs[i][0]))
        liste_2.append(int(inputs[i][1]))

result = 0
# Parcours de la première liste
for a in liste_1 :
    # Ajout du résultat de la multiplication de la valeur courante de la première  liste par son nombre d'apparition dans la seconde
    result += a * liste_2.count(a)

# Affichage du résultat à l'écran
print(result)