with open("9.txt", "r") as f:
    arr = [list(map(int, line.strip().split())) for line in f]



def get_next(seq):
    difs = []
    all_0 = True
    for i in range(len(seq)-1):
        dif = seq[i+1]-seq[i]
        if dif != 0:
            all_0 = False
        difs.append(dif)

    if all_0:
        return seq[-1]
    else:
        return seq[-1] + get_next(difs)

def get_prev(seq):
    difs = []
    all_0 = True
    for i in range(len(seq) - 1):
        dif = seq[i + 1] - seq[i]
        if dif != 0:
            all_0 = False
        difs.append(dif)

    if all_0:
        return seq[0]
    else:
        return seq[0] - get_prev(difs)

t = 0
for nums in arr:
    t += get_prev(nums)

print(t)