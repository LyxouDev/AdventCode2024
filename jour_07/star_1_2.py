
#####################################
# Première/Deuxième Etoile - Jour 7 #
#####################################
        
#Récupération des élements de la fichier d'entrées
with open('input.txt') as input_file:
    inputs = input_file.read().strip()
    
import sys
import re
from collections import defaultdict, Counter, deque

def pr(s):
    print(s)

# Définition de la limite de profondeur maximale de la pile de l'interpréteur Python
sys.setrecursionlimit(10**6)
result_1 = 0
result_2 = 0

def is_valid(target, ns, result_2):
    if len(ns) == 1:
        return ns[0]==target
    if is_valid(target, [ns[0]+ns[1]] + ns[2:], result_2):
        return True
    if is_valid(target, [ns[0]*ns[1]] + ns[2:], result_2):
        return True
    if result_2 and is_valid(target, [int(str(ns[0])+str(ns[1]))] + ns[2:], result_2):
        return True
    return False

for input in inputs.strip().split('\n'):
    target, ns = input.strip().split(':')
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if is_valid(target, ns, result_2=False):
        result_1 += target
    if is_valid(target, ns, result_2=True):
        result_2 += target

pr(result_1)
pr(result_2)
