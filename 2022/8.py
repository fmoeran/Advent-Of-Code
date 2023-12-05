with open("8.txt", "r") as file:
    data = []
    for l in file:
        data.append(list(map(int, list(l.strip()))))
vis = [[False for col in data] for row in data]

t = 0

for r, row in enumerate(data):
    mleft = -1
    for c, tree in enumerate(row):
        if tree > mleft:
            mleft = tree
            vis[r][c] = True
            if mleft == 9:
                break
    mright = -1
    for c, tree in enumerate(row[::-1]):
        if tree > mright:
            mright = tree
            vis[r][len(vis[0])-1-c] = True
            if mright == 9:
                break

for c in range(len(data[0])):
    col = list(map(lambda x: x[c], data))
    mtop = -1
    for r, tree in enumerate(col):
        if tree > mtop:
            mtop = tree
            vis[r][c] = True
            if mtop == 9:
                break
    mbot = -1
    for r, tree in enumerate(col[::-1]):
        if tree > mbot:
            mbot = tree
            vis[len(vis)-1-r][c] = True
#             if mbot == 9:
#                 break
#
# total = 0
# for row in vis:
#     for n in row:
#         total += n
best_score = 0
for r, row in enumerate(data):
    for c, height in enumerate(row):
        total_score = 1
        score = 0
        ncol = c

        while ncol+1 < len(row):
            ncol += 1
            score += 1
            if row[ncol] >= height:
                break
        total_score *= score

        score = 0
        ncol = c

        while ncol-1>= 0:
            ncol -= 1
            score += 1
            if row[ncol] >= height:
                break
        total_score *= score

        score = 0
        nrow = r

        while nrow + 1 < len(row):
            nrow += 1
            score += 1
            if data[nrow][c] >= height:
                break
        total_score *= score

        score = 0
        nrow = r
        while nrow - 1 >= 0:
            nrow -= 1
            score += 1
            if data[nrow][c] >= height:
                break
        total_score *= score

        best_score = max(best_score, total_score)
print(best_score)
