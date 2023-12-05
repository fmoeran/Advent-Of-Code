with open("10.txt", "r") as file:
    data = []
    for l in file:
        data.append(l.strip().split())

nums = [20, 60, 100, 140, 180, 220]
ind = 0
total = 0
x = 1
cycle = 0
crt = [""]


def add_pix():
    global crt
    if len(crt[-1]) == 40:
        crt.append("")
    if abs(x-len(crt[-1])) <= 1:
        crt[-1] += "#"
    else:
        crt[-1] += "."

for line in data:
    cycle += 1
    add_pix()
    if line[0] == "addx":
        cycle += 1
        add_pix()
        x += int(line[1])
print("\n".join(crt))


print(total)