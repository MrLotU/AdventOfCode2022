test_input = '''1
2
-3
3
-2
0
4'''

with open('inputs/20.txt', 'r') as f:
    lines = f.read()

lines = test_input
lines = lines.split('\n')

values = list(enumerate(map(int, lines)))
shadow_values = values[:]

print('---- DAY 20 PART 1 ----')

for val in shadow_values:
    index = values.index(val)
    values.pop(index)
    new_index = (index + val[1]) % len(values)
    values.insert(new_index, val)

v = [x[1] for x in values]
lv = len(v)
i0 = v.index(0)

i1 = (1000 + i0) % lv
i2 = (2000 + i0) % lv
i3 = (3000 + i0) % lv

print(sum(v[x] for x in [i1, i2, i3]))
print('---- DAY 20 PART 2 ----')

values = list(enumerate([x * 811589153 for x in map(int, lines)]))
shadow_values = values[:]

for _ in range(10):
    for val in shadow_values:
        index = values.index(val)
        values.pop(index)
        new_index = (index + val[1]) % len(values)
        values.insert(new_index, val)

v = [x[1] for x in values]
lv = len(v)
i0 = v.index(0)

i1 = (1000 + i0) % lv
i2 = (2000 + i0) % lv
i3 = (3000 + i0) % lv

print(sum(v[x] for x in [i1, i2, i3]))
