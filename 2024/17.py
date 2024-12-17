# WOW. really really fun day. Was a bit stupid and tried to BF part B for way too long. Then tried doing
# a trick with bytes (of size 3 bits) starting from the beginning but the 3rd operation was ruining it. So
# then I realised that working from back to front in the instructions fixed that. Lovely lovely question.
with open("17.txt", "r") as file:
    lines = [line.strip() for line in file]

IP = 0
A = int(lines[0][lines[0].index(":") + 2:])
B = int(lines[1][lines[1].index(":") + 2:])
C = int(lines[2][lines[2].index(":") + 2:])
instructions = list(map(int, lines[-1][lines[-1].index(" "):].split(",")))
c_out = []


def get_combo_op(op):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C


def adv(op):  # 0
    global A
    A >>= get_combo_op(op)


def bxl(op):  # 1
    global B
    B ^= op


def bst(op):  # 2
    global B
    B = get_combo_op(op) % 8


def jnz(op):  # 3
    global IP
    if A != 0:
        IP = op


def bxc(op):  # 4
    global B
    B ^= C


def out(op):  # 5
    c_out.append(get_combo_op(op) % 8)


def bdv(op):  # 6
    global B
    B = A >> get_combo_op(op)


def cdv(op):  # 7
    global C
    C = A >> get_combo_op(op)


opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def get_res(reg_A, reg_B, reg_C):
    global IP, A, B, C, c_out
    IP = 0
    A = reg_A
    B = reg_B
    C = reg_C
    c_out = []
    while IP < len(instructions) - 1:
        opc, oper = instructions[IP], instructions[IP + 1]
        IP += 2
        opcodes[opc](oper)
    return c_out


possible = set()

def dfs(current_A, inst=len(instructions) - 1):
    if inst < 0:
        return
    for a in range(8):
        new_A = current_A * 8 + a
        res = get_res(new_A, 0, 0)
        if res == instructions:
            return new_A
        if res == instructions[inst:]:
            final = dfs(new_A, inst - 1)
            if final is not None:
                return final

a = dfs(0)
print(dfs(0))
