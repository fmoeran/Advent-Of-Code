# this one was kinda boring icl lol

with open("15.txt", "r") as f:
    arr = [line.strip() for line in f]

string = "".join(arr)

vals = string.split(",")



def get_hash(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total = total % 256
    return total


boxes = [[] for _ in range(256)]


def update(val):
    global boxes
    ind = 0
    if "=" in val:
        ind = val.index("=")
    else:
        ind = val.index("-")
    label = val[:ind]
    op = val[ind]

    b = get_hash(label)
    if op == "-":
        for ind, pair in enumerate(boxes[b]):
            if pair[0] == label:
                boxes[b].pop(ind)
                break
    else:
        lens = int(val[-1])
        for ind, pair in enumerate(boxes[b]):
            if pair[0] == label:
                boxes[b][ind][1] = lens
                break
        else:
            boxes[b].append([label, lens])

def get_power(b):
    t = 0
    for ind, pair in enumerate(boxes[b], 1):
        t += (b+1)*ind*pair[1]
    return t
for val in vals:
    update(val)

t= 0
for b in range(256):
    t += get_power(b)
print(t)







