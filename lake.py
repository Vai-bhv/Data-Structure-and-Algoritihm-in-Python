import sys

boat = []

for line in sys.stdin:

    boat.append(line.strip().split())

op = int(boat[0][0])
mdf = int(boat[0][1])

app = False
plo = False
la = []
d = []



for i in range(0, op):
    la.append(1)


for i in range(0, mdf):
    n = int(boat[1][i])
    if boat[1][i] == '0':


        for j in range(i, mdf):

            if boat[1][j] != '0' and la[int(boat[1][j]) - 1] > 0 and app == False:

                la[int(boat[1][j]) - 1] -= 1
                d.append(boat[1][j])
                app = True

        if app == False and i > 0:

            d.append(0)

    else:

        la[n - 1] += 1
        if la[n - 1] > 1:
            print("FLOOD")
            plo = True
            break
    app = False

if plo == False:

    op = ""
    print("OK")

    for i in d:

        op += str(i) + " "
    print(op)
