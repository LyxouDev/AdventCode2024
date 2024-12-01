
############################
# Première Etoile - Jour 1 #
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

# Réorganisez des éléments de la liste par ordre croissant
liste_1.sort()
liste_2.sort()

result = 0
# Parcours des 2 listes de façon simultanée
for a, b in zip(liste_1, liste_2):
    # Ajout de la distance courante à la distance totale
    result += abs(a-b) 

# Affichage du résultat à l'écran
print(result)