with open("4.txt", "r") as f:
    arr = [line[line.index(":")+1:].strip() for line in f]


won = [1] * len(arr)

total = 0
for i, line in enumerate(arr):
    t = 0
    winning = set(map(int, line[:line.index("|")].split()))
    cards = list(map(int, line[line.index("|")+1:].split()))
    for card in cards:
        if card in winning:
            t += 1
    for j in range(1, t+1):
        won[i+j] += won[i]
print(sum(won))


