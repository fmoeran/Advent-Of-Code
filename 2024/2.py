# could've done a nice greedy approach but this was easier to implement and the input size was teeny
# also more vim problems lmao

with open("2.txt", "r") as file:
    lines = [list(map(int, line.strip().split())) for line in file]

t = 0
for line in lines:
    for r in range(len(line)):
        p = line.pop(r)
        safe = True
        inc = line[1] > line[0]
        for i in range(len(line)-1):
            if (line[i+1] <= line[i] and inc) or (line[i+1] >= line[i] and not inc):
                safe = False
            if abs(line[i+1]-line[i]) not in [1, 2, 3]:
                safe = False
        if safe:
            t += 1
            break
        line.insert(r, p)
print(t)


