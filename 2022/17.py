from tqdm import tqdm
with open("17.txt", "r") as file:
    shifts = file.readline().strip()


blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (-1, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (-2, 2), (-1, 2), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]


def shift_block(block, direction):
    for i in range(len(block)):
        block[i] = (block[i][0] + direction[0], block[i][1] + direction[1])


def move_block(block, position, index):
    pos = block[index]
    direction = (position[0]-pos[0], position[1]-pos[1])
    shift_block(block, direction)


def is_block_allowed(block,  positions, left=0, right=7, floor=1):
    for row, col in block:
        if col >= right or col < left:
            return False
        if (row, col) in positions:
            return False
        if row == floor:
            print("hi")
            return False
    return True

placed_positions = set()
highest_position = 1
block_ind = 0
shift_ind = 0
seen_shifts = set()
for _ in tqdm(range(2022)):
    block = blocks[block_ind].copy()
    block_ind = (block_ind+1)%len(blocks)
    shift_block(block, (highest_position-4-block[-1][0], 0))
    shift_block(block, (0, 2))
    while True:
        shift = shifts[shift_ind]
        shift_ind = (shift_ind+1)%len(shifts)
        shift_direction = (0, 1) if shift == ">" else (0, -1)
        shift_block(block, shift_direction)
        if not is_block_allowed(block, placed_positions):
            shift_block(block, (-shift_direction[0], -shift_direction[1]))
        shift_block(block, (1, 0))
        if not is_block_allowed(block, placed_positions):
            shift_block(block, (-1, 0))
            break
    for piece in block:
        placed_positions.add(piece)
        highest_position = min(highest_position, piece[0])

print(-highest_position+1)
print(block_ind, shift_ind)

63414   # height after 5*shifts
126785  # height after 8*shifts



print(len(shifts)*4)