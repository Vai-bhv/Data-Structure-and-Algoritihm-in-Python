def is_valid_move(chessboard, x, y, path):
  # check if the position is within the boundaries of the chessboard
  if x < 0 or x >= len(chessboard) or y < 0 or y >= len(chessboard[0]):
    return False
  # check if the position has not been visited yet
  if chessboard[x][y]:
    return False
  return True
def knight_tour(chessboard, x, y, path, pos):
  moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
  # base case: all positions on the chessboard have been visited
  if pos == m * n:
    return True

  # check all possible moves of the knight
  for move in moves:
    new_x = x + move[0]
    new_y = y + move[1]
    # check if the new position is within the boundaries of the chessboard
    # and has not been visited yet
    if is_valid_move(chessboard, new_x, new_y, path):
      # mark the new position as visited
      chessboard[new_x][new_y] = True
      path.append((new_x, new_y))
      # recursively search for a solution starting from the new position
      if knight_tour(chessboard, new_x, new_y, path, pos + 1):
        return True
      # backtrack: unmark the position and remove it from the path
      chessboard[new_x][new_y] = False
      path.pop()
  return False

# main function
def find_knight_tour(m, n, sx, sy):
  # initialize the chessboard and the path
  chessboard = [[False for _ in range(n)] for _ in range(m)]
  path = [(sx, sy)]
  chessboard[sx][sy] = True
  # start the backtracking search
  if knight_tour(chessboard, sx, sy, path, 1):
    return "ANO"
  else:
    return "NE"

# Read the input
m, n, sx, sy = map(int, input().split())
sx -= 1
sy -= 1
find_knight_tour(m,n,sx, sy)
