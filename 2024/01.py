# no joke lost half my time because the vim clipboard wasn't synced to my windows one so I could copy and paste lmao

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

# with open("1.txt", "r") as file:
#     liens = [map(int, line.strip().split()) for line in file]
#     l1, l2 = [line[0] for line in lines], [line[1] for line in lines]
#     print(sum(map(lambda x: l2.count(x)*x, l1)))