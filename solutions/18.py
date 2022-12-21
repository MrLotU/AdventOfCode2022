import re

test_input = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''

with open('inputs/18.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 18 PART 1 ----')

BOUND_X = -1
BOUND_Y = -1
BOUND_Z = -1

coords = []
for line in lines:
    x, y, z = [int(x) for x in re.findall(r'\d+', line)]
    coords.append([x, y, z])
    BOUND_X = max(x, BOUND_X)
    BOUND_Y = max(y, BOUND_Y)
    BOUND_Z = max(z, BOUND_Z)

area = 0
for coord in coords:
    for i in range(3):
        new_coord = coord[:]
        new_coord[i] += 1
        if new_coord not in coords:
            area += 1
        new_coord = coord[:]
        new_coord[i] -= 1
        if new_coord not in coords:
            area += 1

print(area)

print('---- DAY 18 PART 2 ----')


coord_dict = {}
for coord in coords:
    coord_dict[str(coord)] = True

air_map = set([ str([0,0,0]) ])
coords_to_check = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]

print(BOUND_X, BOUND_Y, BOUND_Z)
for x in range(0, BOUND_X + 1):
    for y in range(0, BOUND_Y + 1):
        for z in range(0, BOUND_Z + 1):
            if str([x,y,z]) in coord_dict or str([x,y,z]) in air_map:
                continue
            
            for offset in coords_to_check:
                new_c = list(map(sum, zip([x,y,z], offset)))
                # print([x,y,z], new_c)
                if str(new_c) in air_map:
                    air_map.add(str([x,y,z]))

print(len(air_map))

area = 0
for coord in coords:
    for i in range(3):
        new_coord = coord[:]
        new_coord[i] += 1
        if str(new_coord) in air_map:
            area += 1
        new_coord = coord[:]
        new_coord[i] -= 1
        if str(new_coord) in air_map:
            area += 1

print(area)
print((BOUND_X+1) * (BOUND_Y + 1) * (BOUND_Z + 1))
print(area + 1)

print( (BOUND_X+1) * (BOUND_Y + 1) * (BOUND_Z + 1) - (area + 1))
