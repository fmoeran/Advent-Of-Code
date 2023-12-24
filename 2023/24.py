# honestly worst day Part A was a breeze, didn't need anything external, just made get_intersection to check if any
# pairs were in the area understood t i needed to do for B but there's no fucking way I'm solving a 9nth degree
# simultanious, tried for a good part of the day lmao. Some people on reddit are saying it can be done with 3/5
# equations, still a piss take had to search up for sim solvers online and found sympy

from sympy import symbols, Eq, solve


class Stone:
    def __init__(self, string):
        string = string.split("@")
        self.pos = list(map(int, string[0].split(",")))
        self.vel = list(map(int, string[1].split(",")))

        self.m = self.vel[1] / self.vel[0]
        self.c = self.pos[1] - self.m * self.pos[0]

    def in_future(self, pos): # used in part A
        for i in range(2):
            if pos[i] - self.pos[i] > 0 and self.vel[i] <= 0:
                return False
            elif pos[i] - self.pos[i] < 0 and self.vel[i] >= 0:
                return False
        return True

# used this for part A
# x(ma-mb) = cb-ca

def get_intersection(a: Stone, b: Stone):
    if a.m == b.m:
        return None
    x = (b.c - a.c) / (a.m - b.m)
    return x, a.m * x + a.c


with open("24.txt", "r") as f:
    arr = [Stone(line.strip()) for line in f]

x = symbols("x")
y = symbols("y")
z = symbols("z")
dx = symbols("dx")
dy = symbols("dy")
dz = symbols("dz")
t1 = symbols("t1")
t2 = symbols("t2")
t3 = symbols("t3")
t4 = symbols("t4")

eq1_1 = Eq(arr[0].pos[0] + arr[0].vel[0] * t1, x + dx * t1)
eq1_2 = Eq(arr[0].pos[1] + arr[0].vel[1] * t1, y + dy * t1)
eq1_3 = Eq(arr[0].pos[2] + arr[0].vel[2] * t1, z + dz * t1)

eq2_1 = Eq(arr[1].pos[0] + arr[1].vel[0] * t2, x + dx * t2)
eq2_2 = Eq(arr[1].pos[1] + arr[1].vel[1] * t2, y + dy * t2)
eq2_3 = Eq(arr[1].pos[2] + arr[1].vel[2] * t2, z + dz * t2)

eq3_1 = Eq(arr[2].pos[0] + arr[2].vel[0] * t3, x + dx * t3)
eq3_2 = Eq(arr[2].pos[1] + arr[2].vel[1] * t3, y + dy * t3)
eq3_3 = Eq(arr[2].pos[2] + arr[2].vel[2] * t3, z + dz * t3)

equations = (eq1_1, eq1_2, eq1_3, eq2_1, eq2_2, eq2_3, eq3_1, eq3_2, eq3_3)

solutions = solve(
    equations,
    (x, y, z, dx, dy, dz, t1, t2, t3))

print(sum(solutions[0][:3]))
