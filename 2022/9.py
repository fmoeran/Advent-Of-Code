with open("9.txt", "r") as file:
    data = []
    for l in file:
        data.append(l.strip().split())


def update(h, t):
    dist = max(abs(h[0] - t[0]), abs(h[1] - t[1]))

    if h[1] == t[1]:
        if h[0] - 1 > t[0]:
            t[0] += 1
        if h[0] + 1 < t[0]:
            t[0] -= 1
    elif h[0] == t[0]:
        if h[1] - 1 > t[1]:
            t[1] += 1
        if h[1] + 1 < t[1]:
            t[1] -= 1
    else:
        if dist > 1:
            if t[0] < h[0]:
                t[0] += 1
            else:
                t[0] -= 1
            if t[1] < h[1]:
                t[1] += 1
            else:
                t[1] -= 1


h = [0, 0]
seen = set()
tails = [[0, 0] for _ in range(10)]

for dir, rate in data:
    for i in range(int(rate)):
        if dir == "U":
            tails[0][0] += 1
        elif dir == "D":
            tails[0][0] -= 1

        elif dir == "R":
            tails[0][1] += 1
        else:
            tails[0][1] -= 1

        for i in range(9):
            update(tails[i], tails[i+1])


        seen.add(tuple(tails[-1]))
    print(tails[-1])
print(len(seen))