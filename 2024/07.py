# cool cool. Could've done part A in honestly 7 minutes but had a typo for 5 mins.
# Had a nice bitmask approach for part A but had to switch to itertools.product when added a 3rd operation :(
# also quite a slow method cant think of anything thatll speed it up much
# UPDATE changed to a dfs appreach with some branch cutting to get it down to 8 seconds.

from time import perf_counter

with open("7.txt", "r") as file:
    lines = [line.strip().split(":") for line in file]


def dfs(required, nums, current_val=0, index=1):
    if index == len(nums):
        return current_val == required
    if index == 1:
        current_val = nums[0]

    new_val = nums[index]
    trials = [current_val + new_val, current_val * new_val, int(str(current_val) + str(new_val))]

    min_val, max_val = current_val, current_val
    for num in nums[index:]:
        if num < 2:
            min_val *= num
        else:
            min_val += num
        max_val = int(str(max_val) + str(num))
    if min_val > required or max_val < required:
        return False

    for trial in trials:
        if dfs(required, nums, trial, index+1):
            return True
    return False

t0 = perf_counter()

total = 0
for l, line in enumerate(lines):
    a = int(line[0])
    b = list(map(int, line[1].split()))
    if dfs(a, b):
        total += a



print(total)

# 10.3 seconds
# 8.2 seconds