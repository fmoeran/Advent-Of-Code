#position
pos = [8, 7]

#scores
score = [0, 0]

role = 0
turn = 0
count = 0

while max(score) < 1000:
    count += 1
    for i in range(3):
        role += 1
        if role == 101: role = 1
        pos[turn] += role
    pos[turn] = pos[turn] % 10
    if pos[turn] == 0: pos[turn] = 10

    score[turn] += pos[turn]
    turn = 1 - turn

print(min(score) * count * 3)

