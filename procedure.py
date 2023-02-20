import sys

def minDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    

def minimum_moves(initialLayout):
    # Initialize the cords for each number
    cords = {
        '1': (0, 0),
        '3': (0, 1),
        '5': (0, 2),
        '2': (1, 0),
        '4': (1, 1),
        '0': (1, 2)
    }
    

    # Initialize the final layout
    finalLayout = '123450'

    # Initialize the total number of moves to 0
    totalMoves = 0

    # Iterate through the initial layout
    for i in range(6):
        initialNumber = initialLayout[i]
        finalNumber = finalLayout[i]


        # If the number is already in the correct position, continue
        if initialNumber == finalNumber:
            continue

        # Get the cords for the initial and final positions
        final_x, final_y = cords[initialNumber]
        initial_x, initial_y = cords[finalNumber]

        # Calculate the Manhattan distance between the initial and final positions
        distance = minDistance(final_x, final_y, initial_x, initial_y)
        
        # Add the distance to the total number of moves
        totalMoves += distance

    return totalMoves

def main():
    # Read the initial layout from standard input
    initialLayout = sys.stdin.readline().strip()
    if '0' not in initialLayout:
        print("NELZE")
        return
    # Print the minimum number of moves
    print(minimum_moves(initialLayout))

if __name__ == '__main__':
    main()
