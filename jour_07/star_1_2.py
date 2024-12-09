
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
p1 = 0
p2 = 0

def is_valid(target, ns, p2):
    if len(ns) == 1:
        return ns[0]==target
    if is_valid(target, [ns[0]+ns[1]] + ns[2:], p2):
        return True
    if is_valid(target, [ns[0]*ns[1]] + ns[2:], p2):
        return True
    if p2 and is_valid(target, [int(str(ns[0])+str(ns[1]))] + ns[2:], p2):
        return True
    return False

for input in inputs.strip().split('\n'):
    target, ns = input.strip().split(':')
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if is_valid(target, ns, p2=False):
        p1 += target
    if is_valid(target, ns, p2=True):
        p2 += target

pr(p1)
pr(p2)