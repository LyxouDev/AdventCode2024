
#############################
# Première Etoile - Jour 12 #
#############################

import os, sys
import time
    
def expand_region(grid: list[list[str]], x: int, y: int, visited_points: set[tuple[int, int]]):
    stack: list[tuple[int, int]] = [(x, y)]
    region: set[tuple[int, int]] = set([(x, y)])
    region_flower = grid[y][x]
    visited_points.add((x, y))
    
    while stack:
        x, y = stack.pop()
        
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                continue

            if grid[new_y][new_x] != region_flower:
                continue

            if (new_x, new_y) in visited_points:
                continue
            
            stack.append((new_x, new_y))
            visited_points.add((new_x, new_y))
            region.add((new_x, new_y))
            
    return len(region), find_perimiter(region)

def find_perimiter(region: set[tuple[int, int]]):
    perimiter = 0
    
    for x, y in region:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy

            if (new_x, new_y) not in region:
                perimiter += 1
    return perimiter
    

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

grid = [list(line) for line in lines]
width = len(grid[0])
height = len(grid)

visited_points: set[tuple[int, int]] = set()
total = 0

for y in range(height):
    for x in range(width):
        if (x, y) in visited_points:
            continue

        perimiters, size = expand_region(grid, x, y, visited_points)
        total += perimiters * size

print(total)
