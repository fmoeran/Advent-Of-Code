with open("6.txt", "r") as f:

    arr = [list(map(int, line[line.index(":")+1:].strip().split())) for line in f]

#part 1
times = arr[0]
dists = arr[1]
total = 1
for i in range(len(times)):
    time, dist = times[i], dists[i]
    k = 0
    for t in range(time):
        if t * (time-t) > dist:
            k += 1
    total *= k
#print(total)


#part 2
time = int("".join([str(t)for t in times]))
dist = int("".join([str(d)for d in dists]))

import math

t0= math.ceil((time-(time*time-4*dist)**0.5)/2)
t1= math.floor((time+(time*time-4*dist)**0.5)/2)

print(t1 -t0 + 1)


