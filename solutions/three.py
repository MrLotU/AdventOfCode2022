test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

with open('inputs/three.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY THREE PART ONE ----')

counter = 0

for line in lines:
    a = []
    l = len(line) / 2
    for i, c in enumerate(line):
        if c not in a and i < l:
            a.append(c)
        if c in a and i >= l:
            score = ord(c)
            if score > 90:
                score = score - 96
            else:
                score = score - 38
            counter += score
            # print(c, score)
            break

print(counter)

print('---- DAY THREE PART TWO ----')

cc = 0
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for chunk in chunks(lines, 3):
    a = []
    for l in chunk[1]:
        if l in chunk[0]:
            a.append(l)
    for l in chunk[2]:
        if l in a:
            score = ord(l)
            if score > 90:
                score = score - 96
            else:
                score = score - 38
            counter += score
            cc += score
            # print(l, score)
            break

print(cc)