test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('inputs/4.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 4 PART 1 ----')

c = 0

for line in lines:
    a, b = line.split(',')
    aa, ab = a.split('-')
    ba, bb = b.split('-')
    aa, ab, ba, bb = int(aa), int(ab), int(ba), int(bb)
    if (aa >= ba and ab <= bb) or (ba >= aa and bb <= ab):
        c += 1

print(c)

print('---- DAY 4 PART 2 ----')

cc = 0

for line in lines:
    a, b = line.split(',')
    aa, ab = a.split('-')
    ba, bb = b.split('-')
    aa, ab, ba, bb = int(aa), int(ab), int(ba), int(bb)

    a, b = range(aa, ab + 1), range(ba, bb + 1)

    if not set(a).isdisjoint(b):
        cc += 1

print(cc)
