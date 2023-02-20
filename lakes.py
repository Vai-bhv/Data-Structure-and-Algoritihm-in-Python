import sys

info = sys.stdin.readline().split(" ")
info = list(info)
info = [int(x) for x in info]
info1 = sys.stdin.readline().split(" ")
info1 = list(info1)
info1 = [int(x) for x in info1]
lakes = []
for i in range(info[0]):
    lakes.append(True)                # true = full

del info[0]
del info[0]

rain = []
norain = []
for i in info1:
    if i != 0:
        rain.append(i)
    else:
        norain.append(i)

flood = False

for i in info1:
    for j in lakes:
        if i == 0 and lakes[rain[0] - 1] == True:
            lakes[rain[0] - 1] = False
            del rain[0]
            norain[i-1] = lakes[rain[0] - 1]
            break
        elif i != 0 and lakes[j] == True:
            flood = True
            break
        elif i != 0 and lakes[j] == False:
            lakes[j] = True
            rain.append(lakes[j])

out = ""

if flood == True:
    print("FLOOD")
else:
    print("OK")
    for i in norain:
        out += i
        out += " "
    print(out)