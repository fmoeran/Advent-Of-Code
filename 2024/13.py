# started VERY slow cause I tried doing a matrix approach for part 1, got confused about when the determinant
# is zero and left to do a brute force approach on a and b. Luckily part b needed the matrix approach and so I checked
# and turns out the test data never lets the determinant of (A, B) be zero, lovely.

with open("13.txt", "r") as file:
    lines = [line.strip() for line in file]

INF = 10000000000000000000


def get_coords(line):
    xs, ys = line.split(",")
    x = int(xs[-1:xs.index("X") + 1:-1][::-1])
    y = int(ys[-1:ys.index("Y") + 1:-1][::-1])
    return x, y


def matmul(m, v):
    return (v[0] * m[0][0] + v[1] * m[0][1],
            v[0] * m[1][0] + v[1] * m[1][1])

M = 100
t = 0

for i in range(0, (len(lines) + 1), 4):
    da = get_coords(lines[i])
    db = get_coords(lines[i + 1])
    end = get_coords(lines[i + 2])
    end = [10000000000000 + end[0], 10000000000000 + end[1]]
    price = INF

    # part A
    # for a in range(M+1):
    #     for b in range(M+1):
    #         if da[0]*a+db[0]*b == end[0] and da[1]*a+db[1]*b == end[1]:
    #             price = min(price, 3*a+b)
    # if price < INF:
    #     t += price

    # part B
    det = da[0] * db[1] - da[1] * db[0]
    if det != 0:
        mat = [[db[1], -db[0]], [-da[1], da[0]]]
        a, b = matmul(mat, end)
        if a % det == 0 and b % det == 0:
            a //= det
            b //= det
            t += 3 * a + b

print(t)
