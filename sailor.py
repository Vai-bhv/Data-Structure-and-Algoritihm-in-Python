import sys

cords = sys.stdin.readline().split()
incex = sys.stdin.readline().split()
cords = [int(x) for x in cords]
incex = [int(x) for x in incex]
incex_1 = cords[0]
incex2 = cords[1]
raft = []
for i in range(incex_1):
    newInput = []
    for j in range(incex_1):
        if i == incex[0] - 1 and j == incex[1] - 1:
            newInput.append(1)
        else:
            newInput.append(0)
    raft.append(newInput)

for k in range(incex2):
    newRaft = []
    for i in range(incex_1):
        newInput = []
        for j in range(incex_1):
            newInput.append(0)
        newRaft.append(newInput)
    for i in range(incex_1):
        for j in range(incex_1):
            if 0 <= (i - 1) < incex_1:
                newRaft[i][j] += raft[i-1][j] * 1/4
            if 0 <= (i + 1) < incex_1:
                newRaft[i][j] += raft[i+1][j] * 1/4
            if 0 <= (j - 1) < incex_1:
                newRaft[i][j] += raft[i][j-1] * 1/4
            if 0 <= (j + 1) < incex_1:
                newRaft[i][j] += raft[i][j+1] * 1/4
    raft = []
    for i in range(incex_1):
        newInput = []
        for j in range(incex_1):
            newInput.append(newRaft[i][j])
        raft.append(newInput)

if incex2 == 0:
    newRaft = raft
p = 0

for i in range(incex_1):
    for j in range(incex_1):
        p += newRaft[i][j]

print('%.3f' % p)