test_input = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

with open('inputs/10.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 10 PART 1 ----')
x = 1
total_ting = 0
second_add = False
iterator = 0
cycle_count = 1

while iterator < len(lines):
    # print(iterator, cycle_count, lines[iterator])
    if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
        print(cycle_count, lines[iterator], x, cycle_count * x)
        total_ting += cycle_count * x
    if lines[iterator] == 'noop':
        iterator += 1
        cycle_count += 1
    else:
        num = int(lines[iterator].split(' ')[-1])
        cycle_count += 1
        if second_add:
            iterator += 1
            x += num
            second_add = False
        else:
            second_add = True
            
print(total_ting)

print('---- DAY 10 PART 2 ----')

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

x = 1
second_add = False
pixels = ''
iterator = 0
cycle_count = 1

while iterator < len(lines):
    # print(iterator, cycle_count, lines[iterator])
    x_coord = (cycle_count % 40) - 1
    if x_coord in (x - 1, x, x + 1):
        pixels += '#'
        # print('#', x_coord, cycle_count, x)
    else:
        pixels += '.'
        # print('.', x_coord, cycle_count, x)
        
    # print(x)
        
    if lines[iterator] == 'noop':
        iterator += 1
        cycle_count += 1
    else:
        num = int(lines[iterator].split(' ')[-1])
        cycle_count += 1
        if second_add:
            iterator += 1
            x += num
            second_add = False
        else:
            second_add = True
            
# print(pixels)
for c in chunks(pixels, 40):
    print(c)