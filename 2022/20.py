from math import ceil
ls = [] # (val, index)
inds = []
zind = -1
with open("20.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        ind = len(inds)
        ls.append((num, ind))
        inds.append(ind)
        if num == 0:
            zind = ind


def shift(ind):
    global ls, inds
    position = inds[ind]
    val, _ = ls[position]
    new_position = position+val
    if new_position < 0:
        dif = -new_position
        inc = ceil(dif/(len(inds)-1))
        new_position += (len(inds)-1)*inc

    if new_position >= len(inds):
        dif = new_position-len(inds)+1
        inc = ceil(dif / (len(inds) - 1))
        new_position -= (len(inds) - 1) * inc
    if new_position == position:
        return
    inc = 1 if new_position > position else -1
    while position != new_position:
        next_position = (position + inc) % len(inds)
        ls[position] = ls[next_position]
        inds[ls[position][1]] = position
        position += inc
    ls[position] = (val, ind)
    inds[ind] = position

def mix():
    for i in range(len(inds)):
        shift(i)


key = 811589153
for i in range(len(inds)):
    ls[i] = (ls[i][0]*key, ls[i][1])

for _ in range(10):
    mix()
    print(_)

s = 0
zind = inds[zind]

for inc in [1000, 2000, 3000]:
    num =ls[(zind+inc)%len(ls)][0]
    s += num
    print(num)
print(s)
