

with open("1.txt", "r") as f:
    arr = [  line.strip() for line in f]


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


total = 0
for s in arr:
    num = ""
    changed = False
    for i, c in enumerate(s):
        if changed:
            break
        if c.isdigit():
            num += c
            changed = True
        for digit in digits:
            if len(s)-i >= len(digit):
                if digit == s[i:i+len(digit)]:
                    num += str(digits.index(digit)+1)
                    changed = True
    changed = False
    for ind, c in enumerate(s[::-1]):
        if changed:
            break
        if c.isdigit():
            num += c
            changed = True
        i = len(s)-ind-1

        for digit in digits:
            if len(s)-i >= len(digit):
                if digit == s[i:i+len(digit)]:
                    num += str(digits.index(digit)+1)
                    changed = True
    total += int(num)

print(total)




