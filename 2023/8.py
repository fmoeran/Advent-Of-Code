# Yeah fuck this question.
# I spent the whole day trying to think of a nice general solution until I realised that they looped back perfectly to the beginning
# How fun...

with open("8.txt", "r") as file:
    direction = file.readline().strip()
    graph = {}
    for line in file.readlines()[1:]:
        a, b, c = line[0:0+3], line[7:7+3], line[12:12+3]
        graph[a] = (b, c)


nodes = []
for node in graph.keys():
    if node[-1] == "A":
        nodes.append(node)

def get_dir(i):
    return 0 if direction[steps[i]%len(direction)] == "L" else 1



def get_steps(start):
    node = start
    steps = 0
    while node[-1] != "Z":
        d = 0 if direction[steps%len(direction)] == "L" else 1
        node = graph[node][d]
        steps += 1
    d = 0 if direction[steps % len(direction)] == "L" else 1
    node = graph[node][d]
    return steps


steps = [0]*len(nodes)


from math import lcm

m = 1
for node in nodes:
    m = lcm(m, get_steps(node))

print(m)