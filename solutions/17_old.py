test_input = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

with open('inputs/17.txt', 'r') as f:
    instructions = f.read()

# instructions = test_input

print(instructions)


class Rock:
    def __init__(self, position, shape) -> None:
        self.position = position
        self.shape = shape
        self.height = len(self.shape.split('\n'))
        self.width = len(self.shape.split('\n')[0])

    def copy(self):
        return Rock(None, self.shape)

    def highest_rel(self):
        highest = [0] * self.width
        for i, line in enumerate(self.shape.split('\n')):
            for x in range(self.width):
                if line[x] == '#':
                    highest[x] = max(highest[x], self.height - i)

        return highest

    def lowest_rel(self):
        lowest = [0] * self.width
        for i, line in enumerate(self.shape.split('\n')):
            for x in range(self.width):
                if line[x] == '#':
                    lowest[x] = self.height - i

        return lowest

    def coords(self):
        ax, ay = self.position
        coords = []
        for i, line in enumerate(self.shape.split('\n')):
            for x in range(self.width):
                if line[x] == '#':
                    coords.append((x + ax, ay + (self.height - i) - 1))

        return coords

    def lowest_abs(self, global_x):
        x, y = self.position

        if global_x < x or global_x >= x + self.width:
            return -1

        rel_lowest = self.lowest_rel()
        rel_x = global_x - x
        return rel_lowest[rel_x] + y - 1

    def height_abs(self, global_x):
        x, y = self.position

        if global_x < x or global_x >= x + self.width:
            return -1

        rel_height = self.highest_rel()
        rel_x = global_x - x
        return rel_height[rel_x] + y - 1

    def check_landing(self, points):
        for global_x, global_y in points.items():
            if self.lowest_abs(global_x) == global_y + 1:
                return True
        
        if global_y == 0:
            return True

        return False

    def move(self, op, megacoords):
        ox, oy = self.position
        if op == 'D':
            self.position = (ox, oy - 1)
            if len([v for v in self.coords() if v in megacoords]) != 0:
                self.position = (ox, oy)
                return True
            return False
        elif op == '>':
            # if (x + self.width - 1 + 1) in points and points[x + self.width - 1 + 1] >= y:
            #     # print('Illegal move cuz overlap >')
            #     return True
            newx = min(7 - self.width, ox + 1)
            self.position = (newx, oy)
        elif op == '<':
            # if (x - 1) in points and points[x - 1] >= y:
            #     # print('Illegal move cuz overlap <')
            #     return True
            newx = max(0, ox - 1)
            self.position = (newx, oy)
        
        if len([v for v in self.coords() if v in megacoords]) != 0:
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
land_on_next = False

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
    print('\n'.join(big_string[:-50:-1]), highest_points, max(highest_points.values()))


while rocks_dropped < 2021:
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index -= len(instructions)
    instruction = instructions[instruction_index]

    if not current_rock:
        current_rock = rocks[rock_index].copy()
        current_rock.position = (2, top_of_last_rock + 4)
        # print('NEW SPAWN: ', current_rock.position)

    # if rocks_dropped == 573:
    #     draw_thing()
    #     if current_rock.position[1] < 846 - 33:
    #         break

    # if rocks_dropped == 603:
    #     draw_thing()
    #     if current_rock.position[1] < 887 - 20:
    #         break
    # print(rocks_dropped, current_rock.position if current_rock else '')
    # draw_thing()
    # print(instruction)

    skip = False
    collision_cancel = current_rock.move(instruction, megacoords)
    if not collision_cancel:
        skip = True
        # Meaning we did a sideways move. Re-check land_on_next
        land_on_next = current_rock.check_landing(highest_points)

    if land_on_next:
        land_on_next = False
        rocks_dropped += 1
        for k, v in highest_points.items():
            highest_points[k] = max(v, current_rock.height_abs(k))
        # print(instruction, highest_points, rock_index,
        #       current_rock.position if current_rock else '')
        # print(current_rock.shape if current_rock else '')
        landed_rocks.append(current_rock)
        for coord in current_rock.coords():
            megacoords[coord] = True
        current_rock = None
        top_of_last_rock = max(highest_points.values())
        rock_index += 1
        if rock_index >= len(rocks):
            rock_index -= len(rocks)
        continue

    if not skip and current_rock.check_landing(highest_points):
        land_on_next = True
        continue

    blocked_down_move = current_rock.move('D', megacoords)

    if current_rock.check_landing(highest_points) or blocked_down_move:
        land_on_next = True

    # print(instruction, highest_points, rock_index,
    #       current_rock.position if current_rock else '')
    # print(current_rock.shape if current_rock else '')

print(highest_points, max(highest_points.values()))

# draw_thing()
print('---- DAY 17 PART 2 ----')
