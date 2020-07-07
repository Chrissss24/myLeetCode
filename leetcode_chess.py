board = [
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]
]

for data in board:
    if "R" in data:
        index = (board.index(data), data.index("R"))
i = index[0]
j = index[1]
row = board[i]
col = []
count = 0
for data in board:
    col.append(data[j])
row_left = row[:j]
row_left.reverse()
row_rigth = row[j + 1:]
if "p" in row_left and "B" not in row_left:
    count += 1
elif "p" in row_left and "B" in row_left and row_left.index("p") < row_left.index("B"):
    count += 1
if "p" in row_rigth and "B" not in row_rigth:
    count += 1
elif "p" in row_rigth and "B" in row_rigth and row_rigth.index("p") < row_rigth.index("B"):
    count += 1

col_up = col[:i]
col_up.reverse()
col_down = col[i + 1:]
if "p" in col_up and "B" not in col_up:
    count += 1
elif "p" in col_up and "B" in col_up and col_up.index("p") < col_up.index("B"):
    count += 1
if "p" in col_down and "B" not in col_down:
    count += 1
elif "p" in col_down and "B" in col_down and col_down.index("p") < col_down.index("B"):
    count += 1

print(count)