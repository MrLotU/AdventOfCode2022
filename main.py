from datetime import date
import importlib
import os

d = date.today().day

TEMPLATE = """test_input = ''''''

with open('inputs/{d}.txt', 'r') as f:
    lines = f.read()

lines = test_input
lines = lines.split('\\n')

print('---- DAY {d} PART 1 ----')

print('---- DAY {d} PART 2 ----')
"""
if f'{d}.py' in os.listdir('solutions'):
    importlib.import_module(f'solutions.{d}')
else:
    with open(f'solutions/{d}.py', 'w') as f:
         f.write(TEMPLATE.format(d=d))
    with open(f'inputs/{d}.txt', 'w') as f:
        pass
    print('Created files')