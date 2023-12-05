with open("3.txt", "r") as f:
    arr = [line.strip() for line in f]

inds = [[-1 for col in row] for row in arr]
nums = []


def get_neighbours(row, col):
    out = []
    for dx in range(-1, 2):

        if 0 <= col + dx < len(arr[0]):
            for dy in range(-1, 2):
                if 0 <= row + dy < len(arr):
                    out.append((row + dy, col+dx))


    return out

total = 0

for row, line in enumerate(arr):
    col = 0
    num = ""
    is_part = False
    for col, c in enumerate(line):

        if c.isdigit():
            num += c
            for neighbour in get_neighbours(row, col):
                d = arr[neighbour[0]][neighbour[1]]
                if not d.isdigit() and d != ".":
                    is_part = True
        if not c.isdigit() or col == len(line)-1:
            if is_part:
                total += int(num)
            if num and is_part:
                nums.append(int(num))
                start = col
                if not c.isdigit():
                    start -= 1
                for ncol in range(start, col-len(num)-1, -1):
                    inds[row][ncol] = len(nums)-1
            num = ""
            is_part = False
t = 0
for row, line in enumerate(arr):
    for col, c in enumerate(line):
        seen = set()
        if c == "*":
            for neighbour in get_neighbours(row, col):
                ind = inds[neighbour[0]][neighbour[1]]
                if ind != -1:
                    seen.add(ind)
        if len(seen) == 2:

            prod = 1
            for i in seen:
                prod *= nums[i]
            t += prod
print(t)

