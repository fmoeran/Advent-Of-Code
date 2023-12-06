from math import ceil

with open("19.txt", "r") as file:
    blueprints = []
    for l in file:
        line = list(map(int, l.strip().split()))
        ore = (line[0], 0, 0)
        clay = (line[1], 0, 0)
        obsidian = (line[2], line[3], 0)
        geode = (line[4], 0, line[5])
        new_bp = (ore, clay, obsidian, geode)
        blueprints.append(new_bp)



def sub(als, bls):
    new = []
    for a, b in zip(als, bls):
        new.append(a - b)
    return tuple(new)


def get_dif(price, materials, rob_counts):
    waits = []
    for i in range(3):
        dif = price[i]-materials[i]

        if rob_counts[i] == 0:
            if dif != 0:
                return None
            else:
                waits.append(1)
        elif dif <= 0:
            waits.append(1)
        else:
            waits.append(1 + ceil((dif)/rob_counts[i]))
    return max(waits)


memo = {}

def max_geode_count(bp, time, rob_counts, mat_counts, max_robots):
    if time <= 0:
        return 0

    m = []
    for i in range(3):
        max_spend = max_robots[i] * time
        m.append(min(max_spend, mat_counts[i]))
    mat_counts = tuple(m)


    hash = (bp, time, *rob_counts, *mat_counts)
    # print(hash)
    res = memo.get(hash)
    if res is not None:
        return res

    # figure out what the new materials will be
    new_mats = []
    for i in range(3):
        new_mats.append(rob_counts[i] + mat_counts[i])
    new_mats = tuple(new_mats)

    ans = max_geode_count(bp, time - 1, rob_counts, new_mats, max_robots)

    for i, robot_prices in enumerate(bp[:-1]):
        if max_robots[i] == rob_counts[i]:
            continue

        wait = get_dif(robot_prices, mat_counts, rob_counts)
        if wait is None:
            continue
        mats_copy = list(mat_counts)
        for j in range(3):
            mats_copy[j] += rob_counts[j] * wait
        mats_copy = tuple(mats_copy)

        new_robots = list(rob_counts)
        new_robots[i] += 1
        new_robots = tuple(new_robots)
        ans = max(ans, max_geode_count(bp, time - wait, new_robots, sub(mats_copy, robot_prices), max_robots))

    wait = get_dif(bp[-1], mat_counts, rob_counts)
    if wait is not None:
        mats_copy = list(mat_counts)
        for j in range(3):
            mats_copy[j] += rob_counts[j] * wait
        mats_copy = tuple(mats_copy)
        if time - wait != 0:
            ans = max(ans, (time - wait) + max_geode_count(bp, time - wait, rob_counts, sub(mats_copy, bp[-1]), max_robots))

    memo[hash] = ans
    return ans


total = 1
for id, bp in enumerate(blueprints[:3]):
    max_robots = [0, 0, 0]
    for i in range(3):
        for prices in bp:
            if prices[i] > max_robots[i]:
                max_robots[i] = prices[i]
    result = max_geode_count(bp, 32, (1, 0, 0), (0, 0, 0), max_robots)
    print(id)
    total *= result
print(total)


