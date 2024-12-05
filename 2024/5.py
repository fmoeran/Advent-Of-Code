# read the question wrong! thought a->b and b->c impies a->c so way overcomplicated it oops.
# anyway fun question especially the second part
with open("5.txt", "r") as file:
    lines = [line.strip() for line in file]
    i = lines.index("")

ahead = [set() for _ in range(100)]

for line in lines[:i]:
    a, b = map(int, line.split("|"))
    ahead[a].add(b)

orders = [list(map(int, line.split(","))) for line in lines[i + 1:]]


def bsort(ls):
    for _ in range(len(ls)):
        for i in range(len(ls) - 1):
            if ls[i] in ahead[ls[i + 1]]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


t = 0

for order in orders:
    valid = True
    for i in range(len(order) - 1):
        if not valid:
            break
        for j in range(i + 1, len(order)):
            if order[i] in ahead[order[j]]:
                valid = False
                break
    if valid:  # part a
        # t += order[len(order)//2]
        pass
    if not valid:  # part b
        order = bsort(order)
        t += order[len(order) // 2]
print(t)
