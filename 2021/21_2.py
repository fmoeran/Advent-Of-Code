import sys

#sys.setrecursionlimit(10000)


rolls = [i+j+k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)]
print(rolls)
def get_key(pos, score, turn):
    return pos[0], pos[1], score[0], score[1], turn


total = 0
memo = {}
def get_wins(pos, score, turn):
    global total
    key = get_key(pos, score, turn)
    if (res := memo.get(key)) is not None:
        total += res[0] + res[1]
        return res


    out = [0, 0]


    if score[1-turn] >= 21:
        total += 1
        out[1-turn] = 1
        return out


    for roll in rolls:
        new_pos = pos[:]
        new_pos[turn] += roll
        if new_pos[turn] > 10: new_pos[turn] = new_pos[turn] %10
        new_score = score[:]
        new_score[turn] += new_pos[turn]
        res = get_wins(new_pos, new_score, 1-turn)

        out[0] += res[0]
        out[1] += res[1]

    memo[key] = out
    return out


#position
pos = [8, 7]

print(max(get_wins(pos, [0, 0], 0)))