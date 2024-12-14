# WOAH!!!! that was awesome. part B I started by displaying every round, then realised that on round 179&282 they
# were pretty compact and same with 105&206, both of which whose differences are the dimensions of the box, so I
#kept on printing the opattern and look what we got!
# its actually the first time that round%103 == 75 and round%101 == 3 which is round ____
# (plus one because they are indexed at 1 but mod indexes at 0)
with open("14.txt", "r") as file:
    lines = [line.strip() for line in file]

robots = []
for line in lines:
    p, v = line.split(" ")
    p = p[2:]
    v = v[2:]
    p = list(map(int, p.split(",")))
    v = list(map(int, v.split(",")))
    robots.append((p, v))

mx, my = 101, 103


# mx, my = 11, 7

def display():
    out = [["."] * mx for _ in range(my)]
    for p, v in robots:
        out[p[1]][p[0]] = "#"
    for row in out:
        print("".join(row))
    print()


for round in range(10_000):
    for i in range(len(robots)):
        p, v = robots[i]
        robots[i] = ([(p[0] + v[0]) % mx, (p[1] + v[1]) % my], v)
    # if round % 103 == 178 % 103 or round % 101 == 104 % 101:
    if round % 103 == 178 % 103 and round % 101 == 104 % 101:
        print(round + 1)
        display()

# part A

quads = [0, 0, 0, 0]

for r, v in robots:
    if r[0] == mx // 2 or r[1] == my // 2:
        continue
    q = 0
    if r[0] > mx // 2:
        q += 1
    if r[1] > my // 2:
        q += 2
    quads[q] += 1

# print(quads[0]*quads[1]*quads[2]*quads[3])

# me keeping track of some interesting rounds
# 179
# 105
# 76
# 282
# 206
