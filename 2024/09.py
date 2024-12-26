# pretty good day. My part B is inefficient, I can see a clever prefix sum x binary search to chop down a factor of n
# in the complexity but CANNOT be asked. So this takes a minute or so to run, take it or leave it.
# UPDATE: improved speed by keeping track of the empty memory. I could still improve this
# with a segment tree or binary search as well.
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
    gaps = [] # (index, length)
    for ind, (l, i) in enumerate(zip(nums, psum)):
        if ind % 2 == 1:
            gaps.append((i, l))
        for j in range(i, i + l):
            used[j] = True

    def defragment():
        nonlocal gaps
        i = 0
        while i < len(gaps)-1:
            if gaps[i][0] + gaps[i][1] == gaps[i+1][0]:
                gaps[i] = (gaps[i][0], gaps[i][1] + gaps[i+1][1])
                gaps.pop(i+1)
            else:
                i += 1
    defragment()

    checksum = 0
    for right in range(len(nums) - (len(nums) % 2), -1, -2):
        rsize = nums[right]
        r_id = right//2
        found = False
        r_pos = psum[right]
        new_pos = r_pos
        for g_ind, (index, length) in enumerate(gaps):
            if index >= r_pos:
                break
            if length >= rsize:
                gaps[g_ind] = (index+rsize, length-rsize)
                found = True
                new_pos = index
                break

        if found:
            for g_ind, (index, length) in enumerate(gaps):
                if index + length == r_pos:
                    new_length = length + rsize
                    if g_ind < len(gaps)-1 and gaps[g_ind+1][0] == index + new_length:
                        new_length = gaps[g_ind+1][1]
                        gaps.pop(g_ind+1)
                    gaps[g_ind] = (index, new_length)
                    break
            # defragment()
        for pos in range(new_pos, new_pos + rsize):
            checksum += pos * r_id
    print(checksum)





part2()

# t = 0
# for ind, val in enumerate(space):
#     if val == -1:
#         continue
#     t += ind * val
# print(t)
