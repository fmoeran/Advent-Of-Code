# pretty good day. My part B is inefficient, I can see a clever prefix sum x binary search to chop down a factor of n
# in the complexity but CANNOT be asked. So this takes a minute or so to run, take it or leave it.
with open("9.txt", "r") as file:
    nums = [list(map(int, line.strip().strip())) for line in file][0]

psum = [0] * len(nums)
for i in range(1, len(nums)):
    psum[i] = psum[i - 1] + nums[i - 1]

space = [-1] * (psum[-1] + nums[-1] + 1)


def part1():
    ind = 0
    left = 0
    right = len(nums) - 1
    if right % 2 == 1:
        right -= 1
    while left <= right:
        if left % 2 == 0:
            for _ in range(nums[left]):
                space[ind] = (left // 2)
                ind += 1

        else:  # left%2 == 1:
            for _ in range(nums[left]):
                if nums[right] == 0:
                    right -= 2
                space[ind] = (right // 2)
                ind += 1
                nums[right] -= 1

    left += 1


def part2():
    used = [False] * len(space)
    for ind, (l, i) in enumerate(zip(nums, psum)):
        if ind % 2 == 1:
            continue
        for j in range(i, i + l):
            used[j] = True

    for right in range(len(nums) - (len(nums) % 2), -1, -2):
        print(right)
        rsize = nums[right]
        rid = right // 2
        done = False
        for i in range(psum[right]):
            if not any(used[i:i + rsize]):
                for j in range(i, i + rsize):
                    used[j] = True
                    space[j] = rid
                done = True
            if done: break
        if not done:
            for j in range(psum[right], psum[right] + rsize):
                used[j] = True
                space[j] = rid


part2()

t = 0
for ind, val in enumerate(space):
    if val == -1:
        continue
    t += ind * val
print(t)
