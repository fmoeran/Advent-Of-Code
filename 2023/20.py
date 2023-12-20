# honestly I hate these types of problems where we don't have enough inf ot o actually do it
# went back to sleep after not seeing a clear solution and woke up and decided to see if they looped at all


from collections import deque

with open("20.txt", "r") as f:
    arr = [line.strip() for line in f]

modules = {}

q = deque([])

counts = [0, 0]

p = 0

trues = {}


class FlipFlop:
    def __init__(self):
        self.name = ""
        self.state = False
        self.outs = []
        self.is_conj = False

    def step(self, state, prev):
        global q, counts

        if not state:
            self.state = not self.state
            for out in self.outs:
                q.append((out, self.state, self.name))


class Conjunction:
    def __init__(self):
        self.name = ""
        self.recents = {}
        self.outs = []
        self.is_conj = True

    def step(self, state, prev):
        global q
        self.recents[prev] = state
        out_s = True
        if self.name == "jq" and state:
            # jq is the conj before rx
            # there are 4 leading into jq
            global p, trues

            trues[prev] = trues.get(prev, []) + [p]

        for val in self.recents.values():
            if not val:
                break
        else:
            out_s = False
        for out in self.outs:
            q.append((out, out_s, self.name))


starts = []

for line in arr:
    pair = line.split(" -> ")
    if pair[0] == "broadcaster":
        starts = pair[1].split(", ")
    elif pair[0][0] == "&":  # conj
        m = Conjunction()
        m.name = pair[0][1:]
        m.outs = pair[1].split(", ")
        modules[m.name] = m
    else:  # flipflop
        m = FlipFlop()
        m.name = pair[0][1:]
        m.outs = pair[1].split(", ")
        modules[m.name] = m

for o in starts:
    m = modules.get(o)
    if m is not None and m.is_conj:
        m.recents["broadcaster"] = False

for module in modules.values():
    for out in module.outs:
        m = modules.get(out)
        if m is not None and m.is_conj:
            m.recents[module.name] = False

states = []


def step():
    global q, counts
    counts[False] += 1
    for out in starts:
        q.append((out, False, "broadcaster"))

    while q:
        mod, state, prev = q.popleft()
        if mod == "rx" and state == False:
            return True
        counts[int(state)] += 1
        m = modules.get(mod)
        if m is not None:
            m.step(state, prev)
    return False


running = True
while running:
    p += 1
    if p % 10000 == 0:
        print(p)
    if step():
        print(p)
        break
    running = not (len(trues) == 4)
    for ls in trues.values():
        if len(ls) < 2:
            running = True

loops = []
for ls in trues.values():
    loops.append(ls[1] - ls[0])

from math import lcm

print(lcm(*loops))
