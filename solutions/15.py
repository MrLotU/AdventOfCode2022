import re
import itertools

test_input = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

with open('inputs/15.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 15 PART 1 ----')

sensors = set()
beacons = set()
impossible_coords = set()

def mh_between(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

for line in lines:
    sx, sy, bx, by = (int(x) for x in re.findall(r'-?\d+', line))
    sensor = (sx, sy)
    sensors.add(sensor)
    beacons.add((bx, by))
    
    mh_distance = mh_between(sensor, (bx, by))
    
    # matrix = list(itertools.product( range(sx - mh_distance, sx + mh_distance + 1), range(sy - mh_distance, sy + mh_distance + 1)  ))
    for xCoord in range(sx - mh_distance, sx + mh_distance + 1):
        coord = (xCoord, 2000000)
        calc_dis = mh_between(sensor, coord)
        # print(calc_dis, mh_distance, coord)
        if calc_dis <= mh_distance and not (coord in sensors or coord in beacons):
            impossible_coords.add(coord)        

print('Line 10: ', len([x for x in impossible_coords if x[1] == 10]))
print('Line 2000000: ', len([x for x in impossible_coords if x[1] == 2000000]))

print('---- DAY 15 PART 2 ----')

max_value = 20
max_value = 4000000

sensors = {}
beacons = set()

# full_matrix = itertools.product(range(0, value + 1), range(0, value + 1))

for line in lines:
    sx, sy, bx, by = (int(x) for x in re.findall(r'-?\d+', line))
    sensor = (sx, sy)
    sensors[sensor] = mh_between(sensor, (bx, by))
    # beacons.add((bx, by))


def p2():
    checked_coords = set()

    for coord, distance in sensors.items():
        sx, sy = coord
        for side in range(4):
            for i in range(distance + 1):
                if side == 0:
                    cx = sx + distance + 1 - i
                    cy = sy + i
                elif side == 1:
                    cx = sx - i
                    cy = sy + distance + 1 - i
                elif side == 2:
                    cx = sx - distance - 1 + i
                    cy = sy - i
                else:
                    cx = sx + i
                    cy = sy - distance - 1 + i

                found = False
                if (0 <= cx <= max_value and 0 <= cy <= max_value and (cx, cy) not in checked_coords):
                    found = all((abs(cx - otherx) + abs(cy - othery)) > other_distance for (otherx, othery), other_distance in sensors.items())

                if found:
                    return max_value * cx + cy
                else:
                    checked_coords.add((cx, cy))
        

# found_coord = None
# y = -1
# skip_until = ()
# for coord in full_matrix:
#     # print(coord)
#     if coord[0] != y:
#         print(coord)
#         y = coord[0]
#     not_this_one = False
#     if coord in beacons or coord in sensors.keys():
#         continue
    
#     for s, d in sensors.items():
#         # print(mh_between(coord, s), d)
#         if mh_between(coord, s) <= d:
#             not_this_one = True
#             break\
    
#     if not_this_one == False:
#         print('found', coord)
#         break
    
    

# print('found', found_coord)
#     mh_distance = mh_between(sensor, (bx, by))
    
#     # xrange = range(max(0, sx-mh_distance), min(sx + mh_distance + 1, 4000000 + 1))
#     # yrange = range(max(0, sy - mh_distance), min(sy + mh_distance + 1, 4000000 + 1))
    
#     xrange = range(max(0, sx-mh_distance), min(sx + mh_distance + 1, 20 + 1))
#     yrange = range(max(0, sy - mh_distance), min(sy + mh_distance + 1, 20 + 1))
    
#     matrix = list(itertools.product(xrange, yrange))
#     for coord in matrix:
#     # for xCoord in range(sx - mh_distance, sx + mh_distance + 1):
#         # coord = (xCoord, 2000000)
#         calc_dis = mh_between(sensor, coord)
#         # print(calc_dis, mh_distance, coord)
#         if calc_dis <= mh_distance and not (coord in sensors or coord in beacons):
#             try:
#                 # full_matrix.remove(coord)
#                 other_full_matrix.remove(coord)
#             except:
#                 pass

print('p2', p2())