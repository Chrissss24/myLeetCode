board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

# print(temp_board)
rows = len(board)
cols = len(board[0])
temp_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
neighbors = [
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
]
for i in board:
    i.insert(0, 0)
    i.append(0)
temp_row = [0 for i in range(cols + 2)]
board.insert(0, temp_row)
board.append(temp_row)
print(board)
print(temp_board)

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        mysum = 0
        if board[i][j] == 1:
            for t in neighbors:
                mysum += board[i + t[0]][j + t[1]]
            if mysum < 2 or mysum > 3:
                temp_board[i-1][j-1] = 0
            elif mysum == 2 or mysum == 3:
                temp_board[i-1][j-1] = 1
        elif board[i][j] == 0:
            for t in neighbors:
                mysum += board[i + t[0]][j + t[1]]
            if mysum == 3:
                temp_board[i-1][j-1] = 1
print(board)
print(temp_board)
board = temp_board
print(board)
print(temp_board)

