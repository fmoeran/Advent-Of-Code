with open("6.txt", "r") as file:
    data = []
    data = file.readlines()[0].strip()

for i in range(len(data)):
    items = data[i:i+14]
    if len(set(items)) == 14:
        print(i+14)
        break

