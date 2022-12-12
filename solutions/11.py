import re
from math import lcm

test_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

with open('inputs/11.txt', 'r') as f:
    lines = f.read()

# lines = test_input
monkeys = lines.split('\n\n')

print('---- DAY 11 PART 1 ----')

inventory = {}
operations = {}
tests = {}

for monkey in monkeys:
    mlines = monkey.split('\n')
    
    monkey_id = int(re.findall(r'\d+', mlines[0])[0])
    
    inventory[monkey_id] = [int(x) for x in re.findall(r'\d+', mlines[1])[::-1]]
    
    operation, by = mlines[2].split(' ')[-2:]
    operations[monkey_id] = '{x} ' + f'{operation} {by if by != "old" else "{x}"}'
    
    div = int(re.findall(r'\d+', mlines[3])[0])
    targets = [int(x) for x in re.findall(r'\d+', '\n'.join(mlines[4:]))[::-1]]
    tests[monkey_id] = (div, targets) # lambda x: targets[x % div == 0]

inspect_counts = {x: 0 for x in inventory.keys()}

for i in range(20):
    for monkey_idx in range(len(monkeys)):
        while len(inventory[monkey_idx]) > 0:
            item = inventory[monkey_idx].pop()
            item = eval(operations[monkey_idx].format(x=item))
            item = item // 3
            d, t = tests[monkey_idx]
            target = t[item % d == 0]
            inspect_counts[monkey_idx] += 1

            inventory[target].insert(0, item)
    
    # print(inventory)
    
sorted_counts = sorted(list(inspect_counts.values()))
print(sorted_counts.pop() * sorted_counts.pop())

print('---- DAY 11 PART 2 ----')

inventory = {}
operations = {}
tests = {}

for monkey in monkeys:
    mlines = monkey.split('\n')
    
    monkey_id = int(re.findall(r'\d+', mlines[0])[0])
    
    inventory[monkey_id] = [int(x) for x in re.findall(r'\d+', mlines[1])[::-1]]
    
    operation, by = mlines[2].split(' ')[-2:]
    operations[monkey_id] = '{x} ' + f'{operation} {by if by != "old" else "{x}"}'
    
    div = int(re.findall(r'\d+', mlines[3])[0])
    targets = [int(x) for x in re.findall(r'\d+', '\n'.join(mlines[4:]))[::-1]]
    tests[monkey_id] = (div, targets) # lambda x: targets[x % div == 0]

inspect_counts = {x: 0 for x in inventory.keys()}
m = lcm(*(x[0] for x in tests.values()))

for i in range(10000):
    print(i, (i // 10000) * 100)
    for monkey_idx in range(len(monkeys)):
        while len(inventory[monkey_idx]) > 0:
            item = inventory[monkey_idx].pop()
            item = eval(operations[monkey_idx].format(x=item))
            item = item % m
            d, t = tests[monkey_idx]
            target = t[item % d == 0]
            inspect_counts[monkey_idx] += 1

            inventory[target].insert(0, item)
    
    print(inventory)
    
sorted_counts = sorted(list(inspect_counts.values()))
print(sorted_counts.pop() * sorted_counts.pop())
