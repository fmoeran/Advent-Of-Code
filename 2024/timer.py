"""
This file times every python file I have in the directory
"""

from time import perf_counter

num_days = 25

with open("times.txt", "w") as times_file:

    for day in range(1, num_days+1):
        t0 = perf_counter()
        sday = str(day).zfill(2)
        print(f'day {sday}')
        exec(open(sday + ".py").read())
        t1 = perf_counter()
        time_taken = round(t1 - t0, 3)
        times_file.write("day " + sday + ": ")
        times_file.write(str(time_taken) +"s\n")

