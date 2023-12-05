nums = [[]]
with open("1.txt", "r") as f:
    for line in f:
        if line.strip():
            nums[-1].append(int(line.strip()))

        else:
            nums.append([])

m = sorted(nums, key=sum, reverse=True)
print(sum(m[0]+m[1]+m[2]))

