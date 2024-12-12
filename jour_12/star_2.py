
#############################
# Deuxième Etoile - Jour 12 #
#############################

from collections import defaultdict
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
    return len(region), find_sides(region)

def find_sides(region: set[tuple[int, int]]):
    sides:  dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)

    for x, y in region:
        vertical_left = (x - 1, y)
        vertical_right = (x + 1, y)
        horizontal_up = (x, y - 1)
        horizontal_down = (x, y + 1)
        
        if vertical_left not in region:
            sides[(x, 0)].add((x, y))
            
        if vertical_right not in region:
            sides[(x, 1)].add((x, y))
            
        if horizontal_up not in region:
            sides[(y, 2)].add((x, y))
            
        if horizontal_down not in region:
            sides[(y, 3)].add((x, y))
    side_count = 0
    
    for section in sides.values():
        visited: set[tuple[int, int]] = set()
        
        for x, y in section:
            if (x, y) not in visited:
                grow_section(x, y, section, visited)
                side_count += 1

    return side_count
    
def grow_section(x: int, y: int, section: set[tuple[int, int]], visited: set[tuple[int, int]]):
    stack: list[tuple[int, int]] = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            
            if (new_x, new_y) not in section:
                continue
            
            if (new_x, new_y) in visited:
                continue
            
            stack.append((new_x, new_y))
            visited.add((new_x, new_y))
    
    
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

        side_count, size = expand_region(grid, x, y, visited_points)
        total += side_count * size
print(total)
