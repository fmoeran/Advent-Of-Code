with open("25.txt", 'r') as file:
    lines = [line.strip() for line in file]
    grids = [[]]
    for line in lines:
        if not line:
            grids.append([])
        else:
            grids[-1].append(line)

locks = []
keys = []

for grid in grids:
    is_lock = (grid[0][0] == '#')
    if not is_lock:
        grid = grid[::-1]
    code = []
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][col] == '.':
                code.append(row-1)
                break

    if is_lock:
        locks.append(code)
    else:
        keys.append(code)

def key_hash(key):
    m = 1
    out = 0
    for val in key[::-1]:
        out += val * m
        m *= 6
    return out

keys.sort()
M_KEYS = key_hash([5, 5, 5, 5, 5]) + 1
key_locations = [-1] * M_KEYS

for i, key in enumerate(keys):
    key_locations[key_hash(key)] = i

for i in range(1, len(key_locations)):
    if key_locations[i] == -1:
        key_locations[i] = key_locations[i-1]

def get_location(key):
    return key_locations[key_hash(key)]

def key_exists(key):
    l = get_location(key)
    if l == -1:
        return False
    return keys[l] == key

def get_children(key, index=0):
    if index == len(key):
        return [key[:]]
    out = []
    temp_key = key[:]
    for v in range(key[index]+1):
        temp_key[index] = v
        out.extend(get_children(temp_key, index+1))
    return out


t = 0
for lock in locks:
    max_key = [5-v for v in lock]
    for child_key in get_children(max_key):
        if key_exists(child_key):
            t += 1

print(t)
