# didn't read "cycle" which slowed me don a bit for p2 lol

with open("14.txt", "r") as f:
    arr = [list(line.strip()) for line in f]


def get_weight():
    out = 0
    for row in range(len(arr)):
        w = len(arr) - row
        out += w * arr[row].count("O")
    return out


def north():
    new_arr = [[char if char != "O" else "." for char in row] for row in arr]
    for row in range(-1, len(new_arr)):
        for col in range(len(new_arr)):
            if row == -1 or new_arr[row][col] == "#":
                inc = 1
                for r in range(row + 1, len(new_arr)):
                    if arr[r][col] == "#":
                        break
                    elif arr[r][col] == "O":
                        new_arr[row + inc][col] = "O"
                        inc += 1
    return new_arr


def west():
    new_arr = [[char if char != "O" else "." for char in row] for row in arr]
    for row in range(len(new_arr)):
        for col in range(-1, len(new_arr)):
            if col == -1 or new_arr[row][col] == "#":
                inc = 1
                for c in range(col + 1, len(new_arr[0])):
                    if arr[row][c] == "#":
                        break
                    elif arr[row][c] == "O":
                        new_arr[row][col + inc] = "O"
                        inc += 1
    return new_arr


def south():
    new_arr = [[char if char != "O" else "." for char in row] for row in arr]
    for row in range(len(new_arr), -1, -1):
        for col in range(len(new_arr)):
            if row == len(new_arr) or new_arr[row][col] == "#":
                inc = 1
                for r in range(row - 1, -1, -1):
                    if arr[r][col] == "#":
                        break
                    elif arr[r][col] == "O":
                        new_arr[row - inc][col] = "O"
                        inc += 1
    return new_arr


def east():
    new_arr = [[char if char != "O" else "." for char in row] for row in arr]
    for row in range(len(new_arr)):
        for col in range(len(new_arr[0]), -1, -1):
            if col == len(new_arr[0]) or new_arr[row][col] == "#":
                inc = 1
                for c in range(col - 1, -1, -1):
                    if arr[row][c] == "#":
                        break
                    elif arr[row][c] == "O":
                        new_arr[row][col - inc] = "O"
                        inc += 1
    return new_arr


tilts = [north, west, south, east]

seen = {}

t = 0


def tilt():
    global arr, t

    string = "".join(["".join(l) for l in arr])

    if (res := seen.get(string)) is not None:

        loop = t - res
        remaining = (4000000000 - t)%loop
        print("hi", t)
        for j in range(remaining%loop):
            arr = tilts[(t+j) % 4]()
        t = 4000000000
        return arr
    seen[string] = t
    arr = tilts[t % 4]()

    t += 1


while t < 4000000000:
    tilt()
print(get_weight())
