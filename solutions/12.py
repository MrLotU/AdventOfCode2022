import re

test_input = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

with open('inputs/12.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

height = len(lines)
width = len(lines[0])

print('---- DAY 12 PART 1 ----')

start = (0,0)
goal = (0,0)
for y, line in enumerate(lines):
    if line.find('S') >= 0:
        start = (line.find('S'), y)
    if line.find('E') >= 0:
        goal = (line.find('E'), y)
        
def value_at(x, y):
    return ord(lines[y][x].replace('S', 'a').replace('E', 'z'))

def get_adjacent_tiles(coord):
    x, y = coord
    tiles = []
    if x != 0:
        tiles.append(((x-1, y), value_at(x-1, y)))
    if x != width - 1:
        tiles.append(((x+1, y), value_at(x+1,y)))
    
    if y != 0:
        tiles.append(((x, y-1), value_at(x, y-1)))
    if y != height - 1:
        tiles.append(((x, y+1), value_at(x, y+1)))
    
    return tiles

print(start, goal)

fields_to_check = [ ( start, value_at(*start), 0 )  ]

checked_coords = set()

while len(fields_to_check) > 0:
    coord, elevation, step = fields_to_check.pop(0)
    
    if coord in checked_coords:
        continue
    checked_coords.add(coord)
    
    if coord == goal:
        print('GOT THERE!', step)
        break
    
    for adjacent, a_height in get_adjacent_tiles(coord):
        if a_height - elevation <= 1:
            fields_to_check.append(( adjacent, a_height, step + 1 ))

            
print('---- DAY 12 PART 2 ----')

starts = []
goal = (0,0)
for y, line in enumerate(lines):
    starts += [(m.start(), y) for m in re.finditer('a', line)]
    if line.find('E') >= 0:
        goal = (line.find('E'), y)

# print(starts)

path_options = []

for start in starts:
    fields_to_check = [ ( start, value_at(*start), 0 )  ]

    checked_coords = set()

    while len(fields_to_check) > 0:
        coord, elevation, step = fields_to_check.pop(0)
        
        if coord in checked_coords:
            continue
        checked_coords.add(coord)
        
        if coord == goal:
            path_options.append(step)
            break
        
        for adjacent, a_height in get_adjacent_tiles(coord):
            if a_height - elevation <= 1:
                fields_to_check.append(( adjacent, a_height, step + 1 ))


print(min(path_options))