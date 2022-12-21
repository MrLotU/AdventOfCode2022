test_input = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

with open('inputs/17.txt', 'r') as f:
    instructions = f.read()

# instructions = test_input

class Rock:
    def __init__(self, position, shape) -> None:
        self.position = position
        self.shape = shape
        self.height = len(self.shape.split('\n'))
        self.width = len(self.shape.split('\n')[0])

    def copy(self):
        return Rock(None, self.shape)

    def coords(self):
        ax, ay = self.position
        coords = []
        for i, line in enumerate(self.shape.split('\n')):
            for x in range(self.width):
                if line[x] == '#':
                    coords.append((x + ax, ay + (self.height - i) - 1))

        return coords

    def move(self, op, megacoords):
        ox, oy = self.position
        if op == 'D':
            self.position = (ox, oy - 1)
        elif op == '>':
            newx = min(7 - self.width, ox + 1)
            self.position = (newx, oy)
        elif op == '<':
            newx = max(0, ox - 1)
            self.position = (newx, oy)
        
        if len([v for v in self.coords() if v in megacoords]) != 0 or self.position[1] < 0:
            self.position = (ox, oy)
            return True
        return False


rocks = [
    Rock(None, '####'),
    Rock(None, '.#.\n###\n.#.'),
    Rock(None, '..#\n..#\n###'),
    Rock(None, '#\n#\n#\n#'),
    Rock(None, '##\n##')
]


print('---- DAY 17 PART 1 ----')

rock_index = 0
instruction_index = -1
current_rock = None
rocks_dropped = 0

top_of_last_rock = -1

megacoords = {}
highest_points = {x: -1 for x in range(7)}

landed_rocks = []

# for rock in rocks:
#     rock.position = (2, 3)
#     print(rock.shape, rock.coords())


def draw_thing():
    all_coords = []
    for landed_rock in landed_rocks:
        c = landed_rock.coords()
        all_coords += c

    cc = None
    if current_rock:
        cc = current_rock.coords()

    big_string = ['+-------+']
    for y in range(max(highest_points.values()) + 7):
        s = '|'
        for x in range(7):
            v = all_coords.count((x, y))
            if v == 1:
                s += '#'
            elif cc and cc.count((x, y)) == 1:
                s += '@'
            elif v == 0:
                s += '.'
            else:
                s += f'{v}'
        s += '|'

        big_string.append(s)
    print('\n'.join(big_string[:-50:-1]), highest_points, max(highest_points.values()) + 1, rocks_dropped)


while rocks_dropped < 2022:
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index -= len(instructions)
    instruction = instructions[instruction_index]

    if not current_rock:
        current_rock = rocks[rock_index].copy()
        current_rock.position = (2, top_of_last_rock + 4)

    # draw_thing()
    
    current_rock.move(instruction, megacoords)
    
    landed = current_rock.move('D', megacoords)
    if landed:
        rocks_dropped += 1
        for x,y in current_rock.coords():
            highest_points[x] = max(highest_points[x], y)
            megacoords[(x,y)] = True
        landed_rocks.append(current_rock)
        current_rock = None
        top_of_last_rock = max(highest_points.values())
        rock_index += 1
        if rock_index >= len(rocks):
            rock_index -= len(rocks)

print(highest_points, max(highest_points.values()) + 1)

draw_thing()
print('---- DAY 17 PART 2 ----')

# rock_index = 0
# instruction_index = -1
# current_rock = None
# rocks_dropped = 0

# top_of_last_rock = -1

# megacoords = {}
# highest_points = {x: -1 for x in range(7)}

# landed_rocks = []

# for rock in rocks:
#     rock.position = (2, 3)
#     print(rock.shape, rock.coords())


while rocks_dropped < 1000000000000:
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index -= len(instructions)
    instruction = instructions[instruction_index]

    if not current_rock:
        current_rock = rocks[rock_index].copy()
        current_rock.position = (2, top_of_last_rock + 4)

    print(rocks_dropped, '{:.2f}%'.format(rocks_dropped / 1000000000000 * 100))
    
    current_rock.move(instruction, megacoords)
    
    landed = current_rock.move('D', megacoords)
    if landed:
        rocks_dropped += 1
        for x,y in current_rock.coords():
            highest_points[x] = max(highest_points[x], y)
            megacoords[(x,y)] = True
        landed_rocks.append(current_rock)
        current_rock = None
        top_of_last_rock = max(highest_points.values())
        rock_index += 1
        if rock_index >= len(rocks):
            rock_index -= len(rocks)

print(highest_points, max(highest_points.values()) + 1)

draw_thing()
