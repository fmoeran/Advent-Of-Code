def get_line(line):#
    num = ""
    out = []
    stack = [out]
    for char in line[1:]:
        if char == "[":
            stack[-1].append([])
            stack.append(stack[-1][-1])
        elif char == "]":
            if num:
                stack[-1].append(int(num))
                num = ""
            stack.pop()
        elif char == ",":
            if num:
                stack[-1].append(int(num))
                num = ""
        else:
            num += char
    return out

with open("13.txt", "r") as file:
    pairs = [[]]
    for l in file:
        line = l.strip()
        if line:
            pairs[-1].append(get_line(line))
        else:
            pairs.append([])

print("", pairs[0][0], '\n', pairs[0][1])
print()

# CHECK IF LEFT < RIGHT
def compare(left, right):
    i = 0
    while i <len(left) and i<len(right):
        l, r = left[i], right[i]
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        else:
            if type(l) == int:
                l = [l]
            if type(r) == int:
                r = [r]
            result = compare(l, r)

            if result is not None:
                return result
        i += 1

    if i == len(left) and i == len(right):
        return None
    elif i == len(left):
        return True
    elif i == len(right):
        return False
#print(len(pairs)**2)
# total = 0
# for ind, pair in enumerate(pairs, 1):
#     result = compare(*pair)
#     if result is True:
#
#         total += ind
#         print(ind)
# print(total)

# sort packets


packets = []
for pair in pairs:
    packets.extend(pair)

packets.append([[2]])
packets.append([[6]])


# SORT PACKETS
changed = True
i = 1
while changed:
    changed = False
    for ind in range(len(packets)-i):
        if not compare(packets[ind], packets[ind+1]):
            packets[ind], packets[ind+1] = packets[ind+1], packets[ind]
            changed = True
    i += 1

k1, k2 = packets.index([[2]])+1, packets.index([[6]])+1
print(k1*k2)
