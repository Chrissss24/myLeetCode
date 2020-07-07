s = "LEETCODEISHIRING"
numRows = 4

col = 1
temp = []
data = []
for i in range(numRows):
    data.append('')
flag = True
j = 0
for i in range(len(s)):
    data[j] += s[i]
    if flag:
        j += 1
    else:
        j -= 1

    if j == numRows - 1 or j == 0:
        flag = not flag
print(''.join(data))
