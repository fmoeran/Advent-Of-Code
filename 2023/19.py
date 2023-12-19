# Made a new file for my p2 today cause I knew basically everything was gonna need a refactor lol


with open("19.txt", "r") as f:
    arr = [line.strip() for line in f]



class Part:
    def __init__(self):
        self.x = [1, 4000]
        self.m = [1, 4000]
        self.a = [1, 4000]
        self.s = [1, 4000]

    def copy(self):
        out = Part()
        out.x = self.x
        out.m = self.m
        out.a = self.a
        out.s = self.s
        return out


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
    t = 1
    t *= max(part.x[1]-part.x[0]+1, 0)
    t *= max(part.m[1]-part.m[0]+1, 0)
    t *= max(part.a[1]-part.a[0]+1, 0)
    t *= max(part.s[1]-part.s[0]+1, 0)
    total += t



def solve(part, workflow):
    w = workflows[workflow]
    for p in w:
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
            can_pass = False
            old_val = a[:]
            if cmp == "<":
                if a[0] < b:
                    new_val = [a[0], min(b-1, a[1])]
                    old_val = [new_val[1]+1, a[1]]
                    can_pass = True
            elif cmp == ">":
                if a[1] > b:
                    can_pass = True
                    new_val = [max(b+1, a[0]), a[1]]
                    old_val = [a[0], new_val[0]-1]



            if can_pass:
                new_part = part.copy()
                if item == "x": new_part.x = new_val
                if item == "m": new_part.m = new_val
                if item == "a": new_part.a = new_val
                if item == "s": new_part.s = new_val
                if res == "A":
                    accept(new_part)
                elif res == "R":
                    reject(new_part)
                else: # new workflow
                    solve(new_part, res)
            if item == "x": part.x = old_val
            if item == "m": part.m = old_val
            if item == "a": part.a = old_val
            if item == "s": part.s = old_val



solve(Part(), "in")

print(total)