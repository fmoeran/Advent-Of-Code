# nice and easy today
# annoying I didn't realise the input was MULTIPLE LINES so I was stuck only doing the first line for a good few minutes
# also fuck off I don't know regex this is so ugly

with open("3.txt", "r") as file:
    s = "\n".join([line for line in file])

t = 0
run = True
for i in range(len(s)-8):
    if s[i:i+4] == "do()":
        run = True
        continue
    if s[i:i+7] == "don't()":
        run = False
        continue
    if not run:
        continue
    if s[i:i+4] != "mul(":
        continue
    j = i+4
    a = ""
    while "0" <= s[j] <= "9":
        a += s[j]
        j += 1
    if s[j] != ",":
        continue
    j +=1
    b = ""
    while "0" <= s[j] <= "9":
        b += s[j]
        j += 1
    if s[j] != ")":
        continue
    t += int(a)*int(b)

print(t)
