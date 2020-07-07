board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
square = ["" for i in range(9)]
for i in range(3):
    temp = [
        board[3*i],
        board[3*i + 1],
        board[3*i + 2]
    ]
    for li in temp:
        square[3*i] += ("".join(li[:3])).replace('.', "")
        square[3*i + 1] += ("".join(li[3:6])).replace('.', "")
        square[3*i + 2] += ("".join(li[6:9])).replace('.', "")

for s in square: # 检查九宫格
    if len(s) > 1:
        temp = list(set(s))
        if len(temp) != len(s):
            print("false1")

for i in range(9): # 检查行
    temp = "".join(board[i]).replace(".", "")
    if len(temp) > 1 and len(list(set(temp))) < len(temp):
        print("false2")

for i in range(9):# 检查列
    temp = ""
    for li in board:
        temp += li[i]
    temp = temp.replace(".", "")
    if len(temp) > 1 and len(list(set(temp))) < len(temp):
        print("false3")

# 官方解
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

