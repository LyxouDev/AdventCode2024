
############################
# Deuxième Etoile - Jour 2 #
############################

#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.readlines()

    for i in range(len(inputs)):
        inputs[i] = inputs[i].split()

result = 0

for line in inputs:
    # Transformation de la liste de caractères en liste d'entier
    inputs_entier = [int(elt) for elt in line]
    
    # Fonction retournant sur la ligne tester est sans danger
    def sans_danger(nums):
        for x, y in zip(nums, nums[1:]):
            if not (1 <= y - x <= 3):
                return False
        return True

    sure = False
    for i in range(len(inputs_entier)):
        nums = inputs_entier[:i] + inputs_entier[i+1:]

        # Test de dangerosité des niveaux de la ligne courante
        if sans_danger(nums) or sans_danger(nums[::-1]):
            sure = True

    if sur:
        result += 1

print(result)