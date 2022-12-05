import re

test_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

with open('inputs/5.txt', 'r') as f:
    lines = f.read()

# lines = test_input
stacks, directions = lines.split('\n\n')

direction_re = re.compile(r'^move (\d+) from (\d+) to (\d+)$', re.MULTILINE)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

print('---- DAY 5 PART 1 ----')
stack_dict = {}
p2_stack_dict = {}
for layer in stacks.split('\n'):
    for stack, value in enumerate(chunks(layer, 4)):
        if len(value) >= 2 and value[1] != '' and value[1].isupper():
            if value[1].isupper():
                stack_dict[stack + 1] = [value[1]] + stack_dict.get(stack + 1, [])
                p2_stack_dict[stack + 1] = [value[1]] + p2_stack_dict.get(stack + 1, [])

for line in directions.split('\n'):
    c, f, t = direction_re.match(line).groups()
    c, f, t = int(c), int(f), int(t)
    take = stack_dict[f][-c:]
    stack_dict[f] = stack_dict[f][:-c]
    
    stack_dict[t] = stack_dict[t] + take[::-1]

a = ''
for k, v in dict(sorted(stack_dict.items())).items():
    a += v[-1]
    
print(a)

print('---- DAY 5 PART 2 ----')

for line in directions.split('\n'):
    c, f, t = direction_re.match(line).groups()
    c, f, t = int(c), int(f), int(t)
    take = p2_stack_dict[f][-c:]
    p2_stack_dict[f] = p2_stack_dict[f][:-c]
    
    p2_stack_dict[t] = p2_stack_dict[t] + take

a2 = ''
for k, v in dict(sorted(p2_stack_dict.items())).items():
    a2 += v[-1]
    
print(a2)
