
######################################
# Première/Deuxième Etoile - Jour 20 #
######################################

import networkx as nx

grid = open('input.txt').read().splitlines()

min_saved = 100

board = {(r,c):ch for r,row in enumerate(grid) for c,ch in enumerate(row) if ch != '#'}
S = [x for x in board if board[x] == 'S'][0]
E = [x for x in board if board[x] == 'E'][0]
board = set(board)

def neighbors(A,k):
  def _manhattan_neighbors(x, y, k):
    points = set()
    for dx in range(-k, k + 1):
        dy = k - abs(dx)
        points.add((x + dx, y + dy))
        points.add((x + dx, y - dy))
    return points
  return _manhattan_neighbors(A[0],A[1],k) & board

G = nx.Graph()
for x in board:
  for n in neighbors(x, 1):
    G.add_edge(x,n)

dS, path = nx.single_source_dijkstra(G, source=S)
path = set(path[E])

def dist(A,B):
  return abs(A[0]-B[0]) + abs(A[1]-B[1])

# Part 1
t = 0
for x in path:
  for y in neighbors(x,2):
    if (dS[y] - dS[x]) - dist(x,y) >= min_saved:
      t += 1
print(t)

# Part 2
t = 0
for x in path:
  for k in range(20+1):
    for y in neighbors(x,k):
      if (dS[y] - dS[x]) - dist(x,y) >= min_saved:
        t += 1
print(t)
