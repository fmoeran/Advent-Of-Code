with open("5.txt", "r") as file:
    rules = []
    stacks = [[] for _ in range(9)]
    lines = file.readlines()
    while lines[-1].strip() != "":
        l = lines.pop().strip().split()
        rules.append(list(map(int, (l[1], l[3], l[5]))))
    lines.pop()
    lines.pop()
    while lines:
        l = lines.pop()
        for i, j in enumerate(range(1, len(l), 4)):
            if l[j] != " ":
                stacks[i].append(l[j])


while rules:
    rule = rules.pop()
    stack = stacks[rule[1]-1]
    move = stack[-rule[0]:]
    for _ in range(rule[0]):
        stack.pop()
    stacks[rule[2]-1] += move


for stack in stacks:
    print(stack[-1], end="")