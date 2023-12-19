with open("19.txt", "r") as f:
    arr = [line.strip() for line in f]



class Part:
    def __init__(self, string):
        string = string[1:-1]
        arr = string.split(",")
        self.x = int(arr[0][2:])
        self.m = int(arr[1][2:])
        self.a = int(arr[2][2:])
        self.s = int(arr[3][2:])


parts = []
workflows = {}
ind = 0
while ind < len(arr):
    line = arr[ind]
    start = line.index("{")
    key = line[:start]
    workflows[key] = line[start+1:-1].split(",")
    l = workflows[key]
    for i in range(len(l)):
        l[i] = l[i].split(":")
        if len(l[i]) > 1:
            l[i][0] = [l[i][0][0], l[i][0][1], int(l[i][0][2:])]
    ind += 1
    if not arr[ind]:
        break



ind += 1
while ind < len(arr):
    parts.append(Part(arr[ind]))
    ind += 1


total = 0

def get_val(part, item):
    if item == "x":
        return part.x
    elif item == "m":
        return part.m
    elif item == "a":
        return part.a
    elif item == "s":
        return part.s

def reject(part):
    pass

def accept(part):
    global total
    total += part.x + part.m + part.a + part.s


def solve(part, workflow):
    w = workflows[workflow]
    for p in w:
        #print(p)
        # reached end
        if len(p) == 1:
            if p[0] == "A":
                accept(part)
                return
            elif p[0] == "R":
                reject(part)
                return
            else:  # new workflow
                solve(part, p[0])
                return
        else: # not end

            item, cmp, b = p[0]
            res = p[1]
            a = get_val(part, item)
            passed = False
            if cmp == "<":
                if a < b:
                    passed = True
            elif cmp == ">":
                if a > b:
                    passed = True
            if passed:
                if res == "A":
                    accept(part)
                    return
                elif res == "R":
                    reject(part)
                    return
                else: # new workflow
                    solve(part, res)
                    return




for part in parts:
    solve(part, "in")
print(total)

