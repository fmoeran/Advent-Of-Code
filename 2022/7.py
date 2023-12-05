with open("7.txt", "r") as file:
    data = []
    for l in file:
        line = l.strip()
        data.append(line.split())

dirs = set()

class Node:
    def __init__(self, name):
        self.name = name
        self.children: list[Node] = []
    def __repr__(self):
        return self.name




stack = [Node("/")]
for line in data[1:]:
    if line[0] == "$":
        if line[1] == "cd":

            if line[2] == "..":
                stack.pop()
            else:
                stack[-1].children.append(Node(line[2]))
                stack.append(stack[-1].children[-1])
    else:
        if line[0] != "dir":
            stack[-1].children.append(int(line[0]))


node = stack[0]
print(node.children)

sums = []

def get_sum(node):
    if type(node) == int:
        return node

    total = 0
    for c in node.children:
        total += get_sum(c)
    global sums
    sums.append(total)
    return total
get_sum(node)

#sums.sort(reverse=True)
total =sums[-1]
#print(total)
dif = 70000000-total
needed = 30000000-dif

print(dif)
print(needed)
sums.sort()
for s in sums:
    if s > needed:
        print(s)
        break

