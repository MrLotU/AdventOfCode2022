from itertools import zip_longest
from functools import cmp_to_key

test_input = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

with open('inputs/13.txt', 'r') as f:
    lines = f.read()

# lines = test_input
pairs = lines.split('\n\n')

def parse_line(line):
    return eval(line)

print('---- DAY 13 PART 1 ----')

right_indices = []

def compare_two_lists(l, r):
    # print(l, r, 'a')
    for lvalue, rvalue in zip_longest(l, r):
        # print(lvalue, rvalue)
        if lvalue is None:
            return True
        if rvalue is None:
            return False
        if isinstance(lvalue, int) and isinstance(rvalue, int):
            if lvalue != rvalue:
                # print(lvalue, rvalue, lvalue < rvalue)
                return lvalue < rvalue
        
        deeper_comp = None
        if isinstance(lvalue, int) and isinstance(rvalue, list):
            deeper_comp = compare_two_lists([lvalue], rvalue)
        if isinstance(lvalue, list) and isinstance(rvalue, int):
            deeper_comp = compare_two_lists(lvalue, [rvalue])
        if isinstance(lvalue, list) and isinstance(rvalue, list):
            deeper_comp = compare_two_lists(lvalue, rvalue)
        if deeper_comp is not None:
            return deeper_comp
        # print('My cock n balls', l, r, lvalue, rvalue, type(lvalue), type(rvalue))
        
            

for idx, pair in enumerate(pairs):
    left, right = pair.split('\n')
    left = parse_line(left)
    right = parse_line(right)
    
    if compare_two_lists(left, right):
        # print(left, right)
        right_indices.append(idx + 1)

print(right_indices)    
print(sum(right_indices))

# print(compare_two_lists([[1], [2,3,4]], [[1], 4]))
print('---- DAY 13 PART 2 ----')

in_list = [
    [[2]],
    [[6]]
]

for pair in pairs:
    left, right = pair.split('\n')
    left = parse_line(left)
    right = parse_line(right)

    in_list.append(left)
    in_list.append(right)

sorted_packets = sorted(in_list, key=cmp_to_key(lambda a,b: -1 if compare_two_lists(a,b) else 1))

marker_a = sorted_packets.index([[2]]) + 1
marker_b = sorted_packets.index([[6]]) + 1

print(marker_a, marker_b, marker_a * marker_b)