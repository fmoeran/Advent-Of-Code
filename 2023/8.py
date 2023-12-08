with open("8.txt", "r") as file:
    direction = file.readline().strip()
    graph = {}
    for line in file.readlines()[1:]:
        a, b, c = line[0:0+3], line[7:7+3], line[12:12+3]
        graph[a] = (b, c)


"""
node = "AAA"
step = 0
while node != "ZZZ":
    d = direction[step%len(direction)]
    if d == "L":
        node = graph[node][0]
    else:
        node = graph[node][1]
    step += 1
"""

nodes = []
for node in graph.keys():
    if node[-1] == "A":
        nodes.append(node)
"""
finished = False

while not finished:
    print(nodes)
    d = direction[step%len(direction)]
    step += 1
    ind = 0 if d == "L" else 1
    finished = True
    for i in range(len(nodes)):
        nodes[i] = graph[nodes[i]][ind]
        if nodes[i][-1] != "Z":
            finished = False
"""

def get_dir(i):
    return 0 if direction[steps[i]%len(direction)] == "L" else 1

def get_key(i):
    return nodes[i], steps[i]%len(direction)

steps = [0]*len(nodes)
cycles = [0]*len(nodes)
ends = [[] for _ in range(len(nodes))]
starts = [0]*len(nodes)
for i in range(len(nodes)):

    seen = {}
    searching = True
    while seen.get(get_key(i)) is None:
        d = get_dir(i)
        seen[get_key(i)] = steps[i]
        steps[i] += 1
        nodes[i] = graph[nodes[i]][d]
        if nodes[i][-1] == "Z":
            ends[i].append(steps[i])


    cycles[i] = steps[i] - seen[(nodes[i], get_dir(i))]
    starts[i] = seen[(nodes[i], get_dir(i))]


big_step = 1
total_steps = 0

class Loop:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length

    def __lt__(self, other):
        return self.length < other.length
    def __repr__(self):
        return str(self.length)
from math import lcm, gcd

loops = sorted([Loop(start, end[-1], length) for start, end, length in zip(starts, ends, cycles)])
for loop in loops:
    print(loop.start, loop.end, loop.length)
for loop in loops:
    while total_steps < loop.start or (total_steps-loop.start)%loop.length != (loop.end-loop.start)%loop.length:
        total_steps += big_step
    big_step = lcm(big_step, loop.length)

print(total_steps)



