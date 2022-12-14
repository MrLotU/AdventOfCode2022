test_input = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

with open('inputs/14.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

sand_entry = (500, 0)

rocks = set()

print('---- DAY 14 PART 1 ----')

for line in lines:
    coords = line.split(' -> ')
    for f, t in zip(coords, coords[1:]):
        fromX, fromY = [int(x) for x in f.split(',')]
        toX, toY = [int(x) for x in t.split(',')]
        rocks.add((fromX, fromY))
        rocks.add((toX, toY))

        for x in range(min(fromX, toX), max(fromX, toX)):
            assert fromY == toY, f'{fromY}, {toY}, {x}, {f}, {t}'
            rocks.add((x, fromY))

        for y in range(min(fromY, toY), max(fromY, toY)):
            assert fromX == toX, f'{fromX}, {toX}, {y}, {f}, {t}'
            rocks.add((fromX, y))

# print(sorted(rocks))

sands_landed = 0
current_grain = None
landed_sands = set()

lowest_point = max([c[1] for c in rocks])


def blocked_below(x, y):
    return (x, y+1) in landed_sands or (x, y+1) in rocks


def blocked_diag_right(x, y):
    return (x+1, y+1) in landed_sands or (x+1, y+1) in rocks


def blocked_diag_left(x, y):
    return (x-1, y+1) in landed_sands or (x-1, y+1) in rocks


while True:
    if current_grain is None:
        current_grain = sand_entry

    x, y = current_grain

    if y >= lowest_point:
        print(f'Fell out of world {x}, {y}')
        break

    if not blocked_below(x, y):
        current_grain = (x, y + 1)
        continue
    
    if not blocked_diag_left(x, y):
        current_grain = (x-1, y+1)
        continue

    if not blocked_diag_right(x, y):
        current_grain = (x+1, y+1)
        continue

    # print(f'Landed at {x}, {y}')
    current_grain = None
    landed_sands.add((x,y))
    sands_landed += 1
    
print(sands_landed)

print('---- DAY 14 PART 2 ----')

floor = lowest_point + 2

sands_landed = 0
current_grain = None
landed_sands = set()

while True:
    if current_grain is None:
        current_grain = sand_entry

    x, y = current_grain

    if y == floor - 1:
        current_grain = None
        landed_sands.add((x,y))
        sands_landed += 1
        # print(f'Floord landed {x}, {y}')
        continue

    if not blocked_below(x, y):
        current_grain = (x, y + 1)
        continue
    
    if not blocked_diag_left(x, y):
        current_grain = (x-1, y+1)
        continue

    if not blocked_diag_right(x, y):
        current_grain = (x+1, y+1)
        continue
    
    if current_grain == sand_entry:
        landed_sands.add((x,y))
        sands_landed += 1
        break

    # print(f'Landed at {x}, {y}')
    current_grain = None
    landed_sands.add((x,y))
    sands_landed += 1
    
print(sands_landed)
