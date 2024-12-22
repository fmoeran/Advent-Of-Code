# fun question, interesting second part because I found like 4 solutions, each one being faster than the last
# by a ton which was very cool. Had one running which would've taken about 10 minutes but then figured out the
# actually fast technique while it was running.
# Also, I've given up on getting up early lol, thats me done for this year
from collections import defaultdict
from itertools import product

with open("22.txt", "r") as file:
    secrets = [int(line.strip()) for line in file]

quads = map(tuple, product(range(-9, 10), repeat=4))
totals = {q: 0 for q in quads}
monkey_dics = [defaultdict(int) for _ in secrets]


def mix_and_prune(s, n):
    return (s ^ n) % 16777216


def iterate(s):
    s = mix_and_prune(s, s << 6)
    s = mix_and_prune(s, s >> 5)
    s = mix_and_prune(s, s << 11)
    return s


t = 0
for monkey_ind, initial in enumerate(secrets):
    secrets = [initial]
    values = [initial % 10]
    difs = [0]
    for _ in range(2000):
        secrets.append(iterate(secrets[-1]))
        values.append(secrets[-1] % 10)
        difs.append(values[-1] - values[-2])
    seen_quads = set()
    for i in range(4, len(secrets)):
        quad = tuple(difs[i - 3:i + 1])
        if quad in seen_quads:
            continue
        seen_quads.add(quad)
        monkey_dics[monkey_ind][quad] = values[i]
    for quad, val in monkey_dics[monkey_ind].items():
        totals[quad] += val

print(max(totals.values()))
