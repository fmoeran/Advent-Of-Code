with open("1.txt", "r") as file:
    lines = [list(map(int, line.strip().split())) for line in file]
    l1 = [line[0] for line in lines]
    l2 = [line[1] for line in lines]


l1.sort()
l2.sort()
s = 0
for val in l1:
    s += l2.count(val)*val

print(s)
