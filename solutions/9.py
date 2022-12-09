test_input = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

with open('inputs/9.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 9 PART 1 ----')

head = (0, 0)
tail = (0, 0)

visited_squares = set([(0, 0)])


def should_move_tail(h, t):
    hx, hy = h
    tx, ty = t
    return abs(hx-tx) >= 2 or abs(hy-ty) >= 2


for line in lines:
    direction, amount = line.split(' ')
    for _ in range(int(amount)):
        offset = 1 * (-1 if direction in ('L', 'D') else 1)

        mod_x = direction in ('L', 'R')
        hx, hy = head
        new_head = (hx + offset if mod_x else hx, hy if mod_x else hy + offset)

        if should_move_tail(new_head, tail):
            tail_offset = -1 if direction in ('R', 'U') else 1
            newx, newy = new_head
            new_tail = (newx + tail_offset if mod_x else newx,
                        newy if mod_x else newy + tail_offset)
            visited_squares.add(new_tail)
            tail = new_tail
        head = new_head

print(len(visited_squares))

print('---- DAY 9 PART 2 ----')

# lines = '''R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20'''.split('\n')

coordinates = [(0, 0)]*10

new_visited_squares = set([(0, 0)])

for line in lines:
    direction, amount = line.split(' ')
    for _ in range(int(amount)):
        main_head = coordinates[0]
        hx, hy = main_head
        if direction == 'L':
            new_head = (hx - 1, hy)
        elif direction == 'R':
            new_head = (hx + 1, hy)
        elif direction == 'U':
            new_head = (hx, hy + 1)
        elif direction == 'D':
            new_head = (hx, hy - 1)

        coordinates[0] = new_head

        for tail_idx in range(1, len(coordinates)):
            a, b = coordinates[tail_idx-1]
            c, d = coordinates[tail_idx]
            while abs(a-c) >= 2 or abs(b-d) >= 2:
                newx, newy = coordinates[tail_idx-1]
                tx, ty = coordinates[tail_idx]
                if abs(newx - tx) > 0:
                    if newx > tx: tx += 1
                    else: tx -= 1

                if abs(newy - ty) > 0:
                    if newy > ty: ty+= 1
                    else: ty -= 1

                coordinates[tail_idx] = (tx, ty)
                c, d = tx, ty
        new_visited_squares.add(coordinates[-1])

print(len(new_visited_squares))
