import operator
import sympy
import re
ops = {'+': operator.add, '*': operator.mul,
       '/': operator.truediv, '-': operator.sub}
test_input = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''

with open('inputs/21.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

monkeys = {}

for line in lines:
    name, value = line.split(': ')
    if not ' ' in value:
        value = int(value)
    monkeys[name] = value

you = 'humn'


def get_value_from_monkey(name):
    m = monkeys[name]
    if isinstance(m, int):
        return m

    a, op, b = m.split(' ')
    return ops[op](get_value_from_monkey(a), get_value_from_monkey(b))


print('---- DAY 21 PART 1 ----')

print(get_value_from_monkey('root'))

print('---- DAY 21 PART 2 ----')

a, _, b = monkeys['root'].split(' ')

# Build equation

eq = f'{a} - {b}'
SYM_X = sympy.symbols('X')
while re.findall(r'[a-z]+', eq):
    replacements = re.findall(r'[a-z]+', eq)
    for r in replacements:
        if r == you:
            eq = eq.replace(r, 'SYM_X')
            continue
        eq = eq.replace(r, f'({monkeys[r]})')

# Solve for SYM_X
print(sympy.solve(eval(eq), SYM_X)[0])