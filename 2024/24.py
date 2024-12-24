# REALLY fun day today. First part had me racking my mind for topological sorting algorithms which was great.
# Second part was interesting. I looked through every pair of x__ and y__ then compared its topological parents with
# what would be expected in an adder and once I found one that didn't fit the pattern I knew it was faulty.
# There's quite a lot of code here because I have both part A and B.
from collections import defaultdict
class Register:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.compute = lambda : None
        self.children = []
        self.op = ""

    def __repr__(self):
        if self.value is not None:
            return self.name + ": " + str(self.value)
        else:
            return self.name + ": " + str(self.children)

def names(ls):
    return [v.name for v in ls]

computes = {"AND": (lambda a, b: a & b),
            "OR": (lambda a, b: a | b),
            "XOR": (lambda a, b: a ^ b)}

registers = {}

def create_reg(name):
    reg = Register(name)
    registers[name] = reg
    return reg

def reg_gate(string):
    r1, op, r2, _, name = string.split()
    reg = registers[name]
    reg.children = [registers[r1], registers[r2]]
    reg.compute = computes[op]
    reg.op = op


INPUT_SIZE = 45 # looked at input date, max is x44

with open("24.txt", "r") as file:
    lines =  file.readlines()
    for line in lines:
        if ":" in line:
            create_reg(line[:3]).value = int(line.strip()[-1])
        elif line.strip():
            create_reg(line.strip()[-3:])
    for line in lines:
        if ":" not in line and line.strip():
            reg_gate(line.strip())


def topo_sort(node, seen):
    out = []
    seen.add(node.name)
    for next_node in node.children:
        if next_node.name in seen:
            continue
        out.extend(topo_sort(next_node, seen))
    out.append(node.name)
    return out


def run():
    for reg1 in registers.values():
        if reg1.value is not None:
            continue
        topo = topo_sort(reg1, set())
        for r in topo:
            reg2 = registers[r]
            if reg2.value is None:
                reg2.value = reg2.compute(reg2.children[0].value, reg2.children[1].value)

def get_a_answer():
    out = 0
    for reg in registers.values():
        if reg.name[0] == "z":
            out += reg.value << int(reg.name[1:])


z_registers = list(filter(lambda x: x.name[0] == "z", registers.values()))
z_registers.sort(key=lambda x: x.name)

faulty = set()


parents = defaultdict(list)
for reg in registers.values():
    for child in reg.children:
        parents[child.name].append(reg)

for z in z_registers:
    if z.op != "XOR":
        faulty.add(z.name)


carries = [None] * INPUT_SIZE

for bit in range(1, INPUT_SIZE):
    x = "x" + str(bit).zfill(2)
    y = "y" + str(bit).zfill(2)
    p_xor, p_and = parents[x]
    if p_xor.op == "AND" or p_and.op == "XOR":
        p_xor, p_and = p_and, p_xor

    if len(parents[p_xor.name]) != 2:
        faulty.add(p_xor.name)
    else:
        pxx = parents[p_xor.name][0]
        if pxx.op != "XOR":
            pxx = parents[p_xor.name][1]
        if pxx.name[0] != "z":
            faulty.add(pxx.name)
    if len(parents[p_and.name]) != 1:
        faulty.add(p_and.name)
    elif (p_or := parents[p_and.name][0]).op != "OR":
        faulty.add(parents[p_and.name][0].name)
    elif len(parents[p_or.name]) != 2:
        faulty.add(p_or.name)


for reg in registers.values():
    if reg.op != "XOR":
        continue
    if reg.name[0] == "z":
        continue
    a, b = reg.children
    if a.op == "XOR" or b.op == "XOR":
        faulty.add(reg.name)


faulty.remove("z45")


print(",".join(sorted(faulty)))
print(len(faulty))