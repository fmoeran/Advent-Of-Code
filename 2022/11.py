from math import lcm
items = [[64],[60, 84, 84, 65], [52, 67, 74, 88, 51, 61], [67, 72],
                [80, 79, 58, 77, 68, 74, 98, 64], [62, 53, 61, 89, 86], [86, 89, 82],
                [92, 81, 70, 96, 69, 84, 83]]

ops = ["*7", "+7", "*3", "+3", "**2", "+8", "+2", "+4"]

tests = [13, 19, 5, 2, 17, 11, 7, 3]
trues = [1, 2, 5, 1, 6, 4, 3, 4]
falses = [3, 7, 7, 2, 0, 6, 0, 5]

mod = lcm(*tests)

# items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
#
# ops = ["*19", "+6", "**2", "+3"]
# tests = [23, 19, 13, 17]
# trues = [2, 2, 1, 0]
# falses = [3, 0, 3, 1]


counts = [0 for _ in range(len(items))]
for round in range(10000):
    for m in range(len(items)):
        ls = items[m]
        counts[m] += len(ls)
        for item in ls:
            new = eval(str(item)+ops[m])
            new %= mod
            test = new%tests[m] == 0
            if test:
                items[trues[m]].append(new)
            else:
                items[falses[m]].append(new)
        items[m].clear()

print(items)

counts.sort(reverse=True)
print(counts[0]*counts[1])