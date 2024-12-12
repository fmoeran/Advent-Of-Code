# finally a non-bruteforceable question! Quite annoyed I knew what to do immediately but had a bug with my dict for ages

from collections import defaultdict

with open("11.txt", "r") as file:
    nums = [list(map(int, line.strip().split())) for line in file][0]

M = 2024

stones = defaultdict(int)
for num in nums:
    stones[num] = 1


def blink():
    global stones
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        s = str(stone)
        if stone == 0:
            new_stones[1] += count
        elif len(s) % 2 == 0:
            new_stones[int(s[:len(s) // 2])] += count
            new_stones[int(s[len(s) // 2:])] += count
        else:
            new_stones[stone * M] += count
    stones = new_stones.copy()


for _ in range(75):
    blink()

t = sum(stones.values())
print(t)
