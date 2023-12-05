"""
This file times every python file I have in the directory
"""


import subprocess

num_days = 5

with open("times.txt", "w") as file:

    for day in range(1, num_days+1):
        res = subprocess.getoutput("time python3 " + str(day)+".py")

        user_time = res[res.index("user")+5:res.index("sys")-1]

        file.write("day " + str(day) + ": ")
        file.write(user_time + "\n")