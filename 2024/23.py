# and yet again, dp is way too op. Decently easy day, but refreshing to have a graph theory question
# that wasn't on a 2D fucking grid oh my god.
# I was actually really quick on this one. Though looking at the leaderboard I still wouldn't have got top 100 sadly.
# Finding max cliques is quite a common question so ofc AI is good at it.
from collections import defaultdict
graph = defaultdict(list)
with open("23.txt", "r") as file:
    for line in file:
        a, b = line.strip().split("-")
        graph[a].append(b)
        graph[b].append(a)


groups = set()

def dfs(current_group, visitable):
    h = tuple(sorted(current_group))
    if h in groups:
        return
    groups.add(h)
    for next_node in visitable:
        if next_node not in current_group:
            dfs(current_group + [next_node], visitable.intersection(set(graph[next_node])))

for node in graph.keys():
    dfs([node], set(graph[node]))

ml = 0
mg = ()
for group in groups:
    if len(group) > ml:
        ml = len(group)
        mg = group
print(",".join(mg))