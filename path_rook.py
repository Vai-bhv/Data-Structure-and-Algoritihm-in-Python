from collections import deque



def bfs(board, start, end):
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque([(start, 0)])
    while queue:
        (row, col), count = queue.popleft()
        visited[row][col] = True
        if (row, col) == end:
            return count
        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            while 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col]!= 'x':
                if visited[new_row][new_col] == False:
                    queue.append(((new_row, new_col), count+1))
                new_row, new_col = new_row + move[0], new_col + move[1]
    return -1


board = []
visited = []
for i in range(8):
    a = []
    for j in range(8):
        a.append(False)
    visited.append(a)


for i in range(8):
    row = input().strip()
    board.append(list(row))

start, end = None, None
for i in range(8):
    for j in range(8):
        if board[i][j] == 'v':
            start = (i, j)
        if board[i][j] == 'c':
            end = (i, j)

result = bfs(board, start, end)
print(result)
