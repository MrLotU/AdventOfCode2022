import itertools

test_input = '''30373
25512
65332
33549
35390'''

with open('inputs/8.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 8 PART 1 ----')

h = len(lines)
w = len(lines[0])

outer_edge = h * 2 + w * 2 - 4
inner_trees = 0

def tac(x, y):
    return lines[x][y]

def check_visible_from_at(x,y, xory, r, o):
    for c in r:
        # print(x,y, c if xory else x, y if xory else c)
        h = tac(c if xory else x, y if xory else c)
        if h >= o:
            return False
    return True
    

for x,y in itertools.product(range(w), range(h)):
    if x in (0, w-1) or y in (0, h-1):
        continue
    current_height = tac(x,y)
    # print(x,y, current_height)
    if check_visible_from_at(x,y, True, range(0, x)[::-1], current_height):
        # print('t')
        inner_trees += 1
        continue
    if check_visible_from_at(x,y, True, range(x+1, w), current_height):
        # print('b')
        inner_trees += 1
        continue
    if check_visible_from_at(x,y, False, range(0, y)[::-1], current_height):
        # print('l')
        inner_trees += 1
        continue
    if check_visible_from_at(x,y, False, range(y+1, h), current_height):
        # print('r')
        inner_trees += 1
        continue
    
    # print('i')

print(outer_edge, inner_trees, outer_edge+inner_trees)

print('---- DAY 8 PART 2 ----')

def get_viewing_distance(x,y, xory, r, o):
    val = 0
    for c in r:
        h = tac(c if xory else x, y if xory else c)
        if h < o:
            val += 1
        if h >= o:
            return val + 1
    return val

all_things = []

for x,y in itertools.product(range(w), range(h)):
    current_height = tac(x,y)
    t = get_viewing_distance(x,y,True, range(0,x)[::-1], current_height)
    b = get_viewing_distance(x,y,True, range(x+1, w), current_height)
    l = get_viewing_distance(x,y,False, range(0,y)[::-1], current_height)
    r = get_viewing_distance(x,y,False, range(y+1, h), current_height)

    score = t*b*l*r
    all_things.append(score)
    # print(x,y, ':', current_height, score)

print(max(all_things))
