test_input = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

with open('inputs/6.txt', 'r') as f:
    lines = f.read()

# lines = test_input

print('---- DAY 6 PART 1 ----')

for i in range(0, len(lines) - 4):
    s = lines[i:i+4]
    if len(set(s)) == len(s):
        print(i+4)
        break

print('---- DAY 6 PART 2 ----')

for i in range(0, len(lines) - 14):
    s = lines[i:i+14]
    if len(set(s)) == len(s):
        print(i+14)
        break