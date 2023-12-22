class Brick:
    def __init__(self, string):
        start, end = string.split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        self.x, self.y, self.z = zip(start, end)
        self.x = sorted(self.x)
        self.y = sorted(self.y)
        self.z = sorted(self.z)

        self.x.sort()

        self.blocks = []

        self.mx = max(self.x, self.y, self.z, key=lambda x: abs(x[1] - x[0]))

        if self.mx == self.x:
            self.blocks = [(x, self.y[0], self.z[0]) for x in range(self.x[0], self.x[1] + 1)]
        elif self.mx == self.y:
            self.blocks = [(self.x[0], y, self.z[0]) for y in range(self.y[0], self.y[1] + 1)]
        if self.mx == self.z:
            self.blocks = [(self.x[0], self.y[0], z) for z in range(self.z[0], self.z[1] + 1)]

    def __iter__(self):
        return iter(self.blocks)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return min(self.z) < min(other.z)


with open("22.txt", "r") as f:
    arr = sorted([Brick(line.strip()) for line in f])



column = {}
holding = [[] for _ in range(len(arr))]
held = [0]*len(arr)
fell = [True]*len(arr)

for ind, brick in enumerate(arr):

    if brick.mx == brick.z:
        key = (brick.x[0], brick.y[0])
        height = column.get(key, [(0, -1)])[-1][0]
        new_heights = list(map(lambda x: x[2], brick.blocks))
        d = new_heights[0] - height - 1
        for i in range(len(new_heights)):
            new_heights[i] -= d
        addition = [(h, ind) for h in new_heights]
        column[key] = column.get(key, []) + addition
    else:
        mx_col, mx_height = (0, 0), -1
        for block in brick:
            key = (block[0], block[1])
            height = column.get(key, [(0, -1)])[-1][0]
            if height > mx_height:
                mx_height = height
                mx_col = key
        new_height = mx_height + 1
        for block in brick:
            col = (block[0], block[1])
            column[col] = column.get(col, []) + [(new_height, ind)]

for col, pairs in column.items():
    for i in range(len(pairs)-1):
        if pairs[i][1] != pairs[i+1][1] and pairs[i][0]+1 == pairs[i+1][0]:
            if pairs[i+1][1] not in  holding[pairs[i][1]]:
                holding[pairs[i][1]].append(pairs[i+1][1])
                held[pairs[i+1][1]] += 1



t = 0
for i in range(len(arr)):
    if len(holding[i]) == 0:
        t += 1
    else:
        for j in holding[i]:
            if held[j] <= 1:

                break
        else:
            t += 1

from collections import deque

def search(start_ind):
    holds = holding[:]
    held_count = held[:]
    fallen = 0
    checking = deque([start_ind])
    while checking:
        fallen += 1
        ind = checking.popleft()
        for new_ind in holds[ind]:
            held_count[new_ind] -= 1
            if held_count[new_ind] == 0:
                checking.append(new_ind)
    return fallen

total = 0
for i in range(len(arr)):
    total += search(i) - 1
print(total)




