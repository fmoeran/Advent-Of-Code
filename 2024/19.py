# I was really slow today. Comletely forgot to add the DP part of my algorithm lol. Other than that, really easy day.
from functools import cache

with open("19.txt", "r") as file:
    lines = [line.strip() for line in file]

available = set(lines[0].split(", "))
to_make = lines[2:]
mx_size = max(len(a) for a in available) + 1


@cache
def dfs(towel, ind=0):
    if ind >= len(towel):
        return 1
    t = 0
    for l in range(1, min(mx_size, len(towel) - ind + 1)):
        sub = towel[ind:ind + l]
        if sub in available and (n := dfs(towel, ind + l)) > 0:
            t += n
    return t


total = 0
for towel in to_make[-2::-1]:
    total += dfs(towel)
print(total)
