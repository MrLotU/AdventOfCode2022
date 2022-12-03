test_input = '''A Y
B X
C Z'''

with open('inputs/2.txt', 'r') as f:
    lines = f.readlines()

# lines = test_input.split('\n')

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

print('---- DAY 2 PART 1 ----')
s = 0
for line in lines:
    o, m = line.split()
    o_score = scores[o]
    m_score = scores[m]
    win = o_score - m_score in (-1, 2)
    s += m_score + (3 if m_score == o_score else 6 if win else 0)

print(s)
    
print('---- DAY 2 PART 2 ----')
second_s = 0
steps = {
    'X': -1,
    'Y': 0,
    'Z': 1
}

for line in lines:
    o, m = line.split()
    o_score = scores[o]
    step = steps[m]
    m_score = o_score + step
    m_score = 3 if m_score == 0 else m_score
    m_score = 1 if m_score == 4 else m_score
    win = o_score - m_score in (-1, 2)
    second_s += m_score + (3 if m_score == o_score else 6 if win else 0)

print(second_s)