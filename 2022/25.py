vals = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}
chars = list("=-012")

def convert(s):
    total = 0
    mult = 1
    for char in s[::-1]:
        total += vals[char] * mult


        mult *= 5
    return total



def convert_back(n):
    if n == 0:
        return ""
    i = 1
    m = 2
    while m<n or -m > n:

        i += 1
        m *= 5
        m += 2


    mult = 5**(i-1)
    max_right = m//5
    if 2*mult - max_right <= n:
        ind = 4
        dif = 2
    elif mult - max_right <= n:
        ind = 3
        dif = 1
    elif 0 - max_right <= n:
        ind = 2
        dif = 0
    elif -mult - max_right <= n:
        ind = 1
        dif = -1
    else:
        ind = 0
        dif = -2
    right_num = convert_back(n - mult*dif)
    right_num = "0"*(i-len(right_num)-1) + right_num
    return chars[ind] + right_num



with open("25.txt", "r") as file:
    nums = []
    for l in file:
        line = l.strip()
        nums.append(convert(line))



print(convert_back(sum(nums)))


