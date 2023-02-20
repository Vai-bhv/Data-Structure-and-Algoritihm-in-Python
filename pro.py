import sys

def minDistance(x1, y1, x2, y2, listr):
    return abs(x1 - x2) + abs(y1 - y2)
    


def minMoves(initialLayout):
    cords = {
        '1': (0, 0),
        '2': (0, 1),
        '3': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '0': (1, 2)
    }
    finalLayout = '123450'
    totalMoves = 0

    for i in range(6):
        initialNumber = initialLayout[i]
        finalNumber = finalLayout[i]
        initialX, initialY = cords[initialNumber]
        finalX, finalY = cords[finalNumber]
        moves = minDistance(initialX, initialY, finalX, finalY, initialLayout)
        totalMoves += moves

    return totalMoves


initialLayout = sys.stdin.readline().strip()
if '0' not in initialLayout:
    print("NELZE")
print(minMoves(initialLayout))

