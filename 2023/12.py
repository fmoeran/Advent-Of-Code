# decently long first half
# It felt cheaty to use lru_cache on second half
# but I think the puzzle was asking for some sort of memo and its fast
# I accidentally got up half an hour late today lmao



from functools import lru_cache

with open("12.txt", "r") as file:
    arr = [line.strip().split(" ") for line in file]

springs = []
groups = []

for i, line in enumerate(arr):
    spring = line[0]
    for _ in range(4):
        spring += "?" + line[0]
    springs.append(spring)
    group = list(map(int, line[1].split(",")))*5
    groups.append(group)


@lru_cache(maxsize=None)
def search(line, spring, group, g, placing=False):
    global groups, springs
    if spring == len(springs[line]):
        if group == 0 and g == len(groups[line])-1:
            return 1
        else:
            return 0
    elif group == 0:
        if springs[line][spring] == "#":
            return 0
        if g == len(groups[line])-1:
            if spring < len(springs[line]) and "#" in springs[line][spring+1:]:
                return 0
            else:
                return 1
        return search(line, spring + 1, groups[line][g + 1], g + 1, False)
    if springs[line][spring] == ".":
        if placing and group != 0:
            return 0
        else:
            return search(line, spring + 1, group, g, False)
    elif springs[line][spring] == "#":
        return search(line, spring + 1, group - 1, g, True)
    else:  # ?
        if placing:
            return search(line, spring + 1, group - 1, g, True)
        else:
            out = search(line, spring+1, group, g, False)
            out += search(line, spring+1, group - 1, g, True)
            return out

total = 0

for line in range(len(arr)):
    total += search(line, 0, groups[line][0], 0)

print(total)

