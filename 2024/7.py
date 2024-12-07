# cool cool. Could've done part A in honestly 7 minutes but had a typo for 5 mins.
# Had a nice bitmask approach for part A but had to switch to itertools.product when added a 3rd operation :(
# also quite a slow method cant think of anything thatll speed it up much

from itertools import product

with open("7.txt", "r") as file:
    lines = [line.strip().split(":") for line in file]

total = 0
for l, line in enumerate(lines):
    #print(l)
    a = int(line[0])
    b = list(map(int, line[1].split()))
    for x in product([0, 1, 2], repeat=len(b)-1):
        t = b[0]
        for i in range(len(b) - 1):
            if x[i] == 0:
                t += b[i + 1]
            elif x[i] == 1:
                t *= b[i + 1]
            else:
                t = int(str(t) + str(b[i+1]))
            if t > a:
                break
print(total)
