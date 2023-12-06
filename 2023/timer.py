"""
This file times every python file I have in the directory
"""



from time import perf_counter

num_days = 6

with open("times.txt", "w") as file:

    for day in range(1, num_days+1):
        t0 = perf_counter()
        exec(open(str(day) + ".py").read())
        t = perf_counter()
        time = round(t - t0, 4)
        file.write("day " + str(day) + ": ")
        file.write(str(time) +"s\n")