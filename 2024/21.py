# Wow what a day. Travelling today so could only work on the problem in the afternoon, there goes my streak :(
# I took a really long time on part B. I initially had the right idea just implemented so badly that I
# couldnt't figure out how to memoize it. Then I made some stupid assumption to make it easier which didn't work so
# finally I went back to my original technique and it worked.
from functools import lru_cache
INF= 10000000000000000000
with open("21.txt", "r") as file:
    codes = [line.strip() for line in file]


numpad_locations = {
    "0": (3, 1), "A": (3, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (0, 0), "8": (0, 1), "9": (0, 2)
}


direction_locations = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

def get_paths(start, end, avoid_bl=False, avoid_tl=False):
    d = (end[0]-start[0], end[1]-start[1])
    inc = [0, 0]
    chrs = ["", ""]
    if d[0] < 0:   # up
        inc[0] = -1
        chrs[0] = "^"
    else: # down
        inc[0] = 1
        chrs[0] = "v"

    if d[1] >= 0:   # right
        inc[1] = 1
        chrs[1] = ">"
    else: # left
        inc[1] = -1
        chrs[1] = "<"
    def sub_get_paths(row, col):
        if (row, col) == (0, 0) and avoid_tl:
            return []
        if (row, col) == (3, 0) and avoid_bl:
            return []
        if (row, col) == end:
            return [""]
        out = []
        if row != end[0]:
            for path in sub_get_paths(row+inc[0], col):
                out.append(chrs[0] + path)
        if col != end[1]:
            for path in sub_get_paths(row, col+inc[1]):
                out.append(chrs[1] + path)
        return out
    return sub_get_paths(*start)


def get_future_cost(path, pos_dic):
    out = 0
    path = "A" + path
    for i in range(1, len(path)):
        a = pos_dic[path[i-1]]
        b = pos_dic[path[i]]
        out += abs(a[0]-b[0]) + abs(a[1]-b[1])
    return out

def get_parent_paths(direction_path, on_numpad=False, return_to_A=False):
    if on_numpad:
        pos_dic = numpad_locations
        avoid_bl, avoid_tl = True, False
    else:
        pos_dic = direction_locations
        avoid_bl, avoid_tl = False, True

    if return_to_A:
        direction_path += "A"

    pos = pos_dic["A"]
    paths = [""]

    for next_pos in map(lambda x: pos_dic[x], direction_path):
        paths_refresh = []
        sub_paths = [path + "A" for path in get_paths(pos, next_pos, avoid_bl, avoid_tl)]
        for sub_path_b in sub_paths:
            for sub_path_a in paths:
                paths_refresh.append(sub_path_a + sub_path_b)
        paths = paths_refresh
        pos = next_pos
    return paths

@lru_cache(None)
def min_sub_length(sub, n): # includes adding an A to the end of the sub
    if n == 0:
        return len(sub) + 1
    paths = get_parent_paths(sub, return_to_A=True)
    best = INF
    for path in paths:
        current = 0
        child_subs = path.split("A")
        child_subs.pop() # ignore last empty string
        for child_sub in child_subs:
            current += min_sub_length(child_sub, n-1)
        best = min(best, current)
    return best

def fast_length2(initial_path, n):
    initial_subs = initial_path.split("A")
    total = 0
    for sub in initial_subs:
        total += min_sub_length(sub, n)
    return total - 1


t = 0
for code in codes:
    m = INF
    for patha in get_parent_paths(code, on_numpad=True):
        for pathb in get_parent_paths(patha):
            l = fast_length2(pathb, 24)
            m = min(m, l)
    t += m * int(code[:3])
    print(m)
print(t)
