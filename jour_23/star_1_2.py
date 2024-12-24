
######################################
# Première/Deuxième Etoile - Jour 23 #
######################################

InputList = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip().split("-")
        A, B = Line
        InputList.append((A, B))

ComputerSet = set()
TComputerSet = set()
ComputerLinkDict = {}
for u in InputList:
    for y in u:
        if y not in ComputerSet:
            ComputerSet.add(y)
            ComputerLinkDict[y] = set()
        if y.startswith("t"):
            TComputerSet.add(y)
    A,B = u
    ComputerLinkDict[A].add(B)
    ComputerLinkDict[B].add(A)
    ComputerLinkDict[A].add(A)
    ComputerLinkDict[B].add(B)

NumComputers = len(ComputerSet)
NonTComputerSet = ComputerSet - TComputerSet
SemiSortComputerList = list(TComputerSet) + list(NonTComputerSet)

Part1Answer = 0
ConnectionSet = set()
for a in range(NumComputers-2):
    CompA = SemiSortComputerList[a]
    for b in range(a+1, NumComputers-1):
        CompB = SemiSortComputerList[b]
        if CompB not in ComputerLinkDict[CompA]:
            continue
        for c in range(b+1,NumComputers):
            CompC = SemiSortComputerList[c]
            if CompC not in ComputerLinkDict[CompA] or CompC not in ComputerLinkDict[CompB]:
                continue
            if a < len(TComputerSet):
                Part1Answer += 1
            ConnectionSet.add((CompA, CompB, CompC))

ConnectionList = list(ConnectionSet)
Cont = True
while Cont:
    Cont = False
    NewLANs = set()
    for a in range(len(ConnectionList)):
        if a % 1000 == 300:
            pass
        if ConnectionList[a] == "Void":
            continue
        for b in range(a+1, len(ConnectionList)):
            LANA = ConnectionList[a]
            LANB = ConnectionList[b]
            if LANA == "Void" or LANB == "Void":
                continue
            MergeSet = set(LANA) | set(LANB)
            Target = len(MergeSet)
            NeighborSet = ComputerLinkDict[LANA[0]].copy()
            for m in MergeSet:
                NeighborSet = NeighborSet & ComputerLinkDict[m]
            if len(NeighborSet) < Target:
                continue
            NewList = list(MergeSet)
            NewList.sort()
            ConnectionList[a] = tuple(NewList)
            ConnectionList[b] = "Void"
            Cont = True

    for t in reversed(range(len(ConnectionList))):
        if ConnectionList[t] == "Void":
            del ConnectionList[t]

MaxLength = 0
for c in ConnectionList:
    if len(c) > MaxLength:
        MaxLength = len(c)
        FinalLan = c

Part2Answer = ",".join(FinalLan)

print(f"part 1: {Part1Answer}")
print(f"part 2: {Part2Answer}")
