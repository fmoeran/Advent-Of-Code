from tqdm import tqdm

with open("17.txt", "r") as file:
    shifts = file.readline().strip()

blocks = [
    0b1111,
    0b0100000111000001,
    0b001000000100001110000,
    0b1000000100000010000001,
    0b110000011,
]

left_shifts = [1, 3, -2, 4, 3]

buffer_height = 1000
buffer = 0
for _ in range(buffer_height * 7):
    buffer <<= 1
    buffer += 1


def printmap(num):
    grid = [['.' for _ in range(7)] for row in range(buffer_height)]
    pos = 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if pos & num:
                grid[row][col] = "#"
            pos <<= 1
    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
    print("\n".join(grid)[::-1])
    print()


def get_height(i):
    if i == 0:
        return 0
    h = 0
    while i:
        i >>= 7
        h += 1
    return h


def get_lowpoint(num):
    return num & -num


right_wall = 0
for _ in range(buffer_height+5):
    right_wall <<= 7
    right_wall += 1
left_wall = 0
for _ in range(buffer_height+5):
    left_wall <<= 7
    left_wall += 64

floor = 0b1111111

placed_map = 0

block_ind = 0
shift_ind = 0
current_base_height = 0


seen_positions = {}

differences = {}

def step(block_num):
    global block_ind, shift_ind, placed_map, current_base_height
    hash = (block_ind, shift_ind, placed_map)
    memo_res = seen_positions.get(hash)
    if memo_res is not None:
        differences[hash] = (current_base_height - memo_res[0], block_num-memo_res[1])
        return True
    else:
        seen_positions[hash] = (current_base_height, block_num)


    block = blocks[block_ind]
    map_height = get_height(placed_map)
    new_height = map_height + 3
    block <<= new_height * 7 + left_shifts[block_ind]

    while True:
        shift = shifts[shift_ind]
        shift_ind = (shift_ind+1)%len(shifts)
        shift_ind
        if shift == ">":
            if block & right_wall == 0 and (block >> 1) & placed_map == 0:
                block >>= 1
        else:
            if block & left_wall == 0 and (block << 1) & placed_map == 0:
                block <<= 1


        if block>>7&placed_map != 0 or block & floor != 0:
            break
        else:
            block >>= 7
    placed_map |= block
    block_ind = (block_ind + 1)%len(blocks)
    new_height = get_height(placed_map)
    if new_height > buffer_height:
        dif = new_height - buffer_height
        placed_map >>= 7*dif
        current_base_height += dif

block_num = 0
while True:
    if step(block_num) is True:
        break
    block_num += 1

# the repetition
(rblock_ind, rshift_ind, rplaced_map), (gain, repeat) = list(differences.items())[0]
print(gain, repeat)
# does not include the last few blocks to be placed
almost_height = (1000000000000-block_num)//repeat * gain + get_height(rplaced_map) + current_base_height

placed_map = rplaced_map

block_ind = rblock_ind
shift_ind = rshift_ind
current_base_height = 0
for _ in range((1000000000000-block_num)%repeat):
    seen_positions.clear()
    step(_)

print(almost_height + current_base_height)