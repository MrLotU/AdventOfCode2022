test_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

with open('inputs/7.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')


def get_path(d, p, default=None):
    return d.get('/'.join(p), default)


def set_path(d, p, v):
    d['/'.join(p)] = v


def continuous_sum(d, p, a):
    set_path(d, p, get_path(d, p, default=0) + a)


print('---- DAY 7 PART 1 ----')

location = []
storage_table = {}
dir_table = {}

for line in lines:
    if line.startswith('$'):
        cmd = line[2:]
        if cmd.startswith('cd'):
            d = cmd.split(' ')[-1]
            if d == '..':
                location.pop()
            elif d == '/':
                location = ['~']
            else:
                location.append(d)
    else:
        size, name = line.split(' ')
        if size != 'dir':
            size = int(size)
            set_path(storage_table, location + [name], size)
            for i, e in enumerate(location):
                continuous_sum(dir_table, location[:i+1], size)

# print(storage_table)
# print(dir_table)

c = 0

for v in dir_table.values():
    if v <= 100000:
        c += v

print(c)

print('---- DAY 7 PART 2 ----')

total_space = 70000000
needed_space = 30000000
used_space = dir_table['~']
available_space = total_space - used_space

sorted_sizes = sorted(dir_table.values())

for v in sorted_sizes:
    if available_space + v >= needed_space:
        print(v)
        break
