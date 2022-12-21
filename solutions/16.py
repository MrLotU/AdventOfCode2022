from dataclasses import dataclass
import re
from typing import List, Dict
from collections import deque

test_input = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

with open('inputs/16.txt', 'r') as f:
    lines = f.read()

lines = test_input
lines = lines.split('\n')

@dataclass
class Valve():
    id: str
    rate: int
    exits: List[str]
    
@dataclass
class State():
    minute: int
    position: str
    opened: List[str]
    rate: int
    total: int
    
    def flow(self, end=30):
        return self.total + (end - self.minute + 1) * self.rate
        

valves = {} # type: Dict[str, Valve]
r = re.compile(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
for line in lines:
    groups = r.search(line.strip()).groups()
    id = groups[0]
    rate = int(groups[1])
    tunnels = groups[2].split(', ')
    print(tunnels)
    valves[id] = Valve(id, rate, tunnels)

# def distance_between_valves(a, b):
#     if a == b: return 0
#     visited = set()
#     visited.add(a)
#     to_visit = deque()
#     for tunnel in valves[a].exits:
#         visited.add(tunnel)
#         to_visit.append((tunnel, 1))
    
#     while len(to_visit) > 0:
#         v, steps = to_visit.popleft()
#         if v == b: return steps
#         for t in valves[v].exits:
#             if t not in visited:
#                 visited.add(t)
#                 to_visit.append((t, steps + 1))
        
#     print(f'No path from {a} to {b}')
#     return None
    
# distances = {}
# useful_valves = [v.id for v in valves.values() if v.rate > 0]

# for valve in valves.keys():
#     distances[valve] = {}
#     for d in useful_valves:
#         distances[valve][d] = distance_between_valves(valve, d)

# initial = State(0, 'AA', [], 0, 0)
# max_flow = 0
# states = [initial]

# while len(states):
#     state = states.pop()
#     max_flow = max(max_flow, state.flow())
#     valve = valves[state.position]
#     if state.minute == 30:
#         continue
#     if state.position not in state.opened and valve.rate > 0:
#         states.append(
#             State(state.minute + 1, state.position, state.opened[:] + [state.position], state.rate + valve.rate,
#                     state.total + state.rate))
#         continue
#     for dest_valve in useful_valves:
#         if dest_valve in state.opened:
#             continue
#         distance = distances[state.position][dest_valve]
#         if (state.minute + distance) > 29:
#             continue
#         states.append(State(state.minute + distance, dest_valve, state.opened, state.rate,
#                                     state.total + (state.rate * distance)))
    
    
# print(max_flow)

print('---- DAY 16 PART 1 ----')

# 1. Calc all possible paths
# 2. Loop over paths and calc pressure
# 3. Grab highest number

# total_minutes = 30
# time = 0
# while time < total_minutes:
    
    
#     time += 1    

print('---- DAY 16 PART 2 ----')
