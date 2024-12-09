
############################
# Première Etoile - Jour 9 #
############################

F,S,p=[],[],0

for i, c in enumerate(open('input.txt').read().strip()):
    [F,S][i%2] += [[*range(p,p:=p+int(c))]]

S = sum(S,[])
for f in reversed(F):
    for x in reversed(range(len(f))):
        if len(S) and f[x] > S[0]:
            f[x] = S[0]
            S = S[1:]

print(sum((i*j) for i,f in enumerate(F) for j in f))
