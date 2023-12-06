with open("15.txt", "r") as file:
    pairs = []
    for l in file:
        line = list(map(int, l.strip().split()))
        pairs.append(((line[0], line[1]), (line[2], line[3])))




def dist(x, y, ex, ey):
    return abs(x-ex) + abs(y-ey)

seen = set()
beacons = set()

max_dist = 4000000

x, y = 3303271, 2906101

for sensor, beacon in pairs:
    sensor_dist = dist(*sensor, *beacon)
    pos_dist = dist(*sensor, x, y)
    if pos_dist <= sensor_dist:
        print("no")
