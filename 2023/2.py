with open("2.txt", "r") as f:
    arr = []
    for num, line in enumerate(f):
        text = line[line.index(":")+2:].strip()
        vec = text.split("; ")
        for i in range(len(vec)):
            vec[i] = vec[i].split(", ")
        arr.append(vec)


clr = ["red", "green", "blue"]

t = 0
for id, game in enumerate(arr, 1):
    mx = [0, 0, 0]
    for go in game:

        for item in go:
            num, colour = item.split()
            num = int(num)
            mx[clr.index(colour)] = max(mx[clr.index(colour)], num)
            #if int(num) > mx[clr.index(colour)]:
            #    valid = False
    power = mx[0] * mx[1] * mx[2]
    t += power
    #if valid:
    #    t += id



print(t)



