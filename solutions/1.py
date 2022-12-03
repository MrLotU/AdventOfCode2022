test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

with open('inputs/1.txt', 'r') as f:
    lines = f.read()

# elves = test_input.split('\n\n')
elves = lines.split('\n\n')

print('---- DAY 1 PART 1 ----')

elf_counts = []

for elf in elves:
    elf_counts.append(
        sum([int(x) for x in elf.split('\n')])
    )

print(max(elf_counts))

print('---- DAY 1 PART 2 ----')

sorted_counts = sorted(elf_counts, reverse=True)

print(sum(sorted_counts[:3]))
