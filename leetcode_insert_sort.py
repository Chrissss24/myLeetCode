data = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
result = [data[0]]

for i in data[1:]:
    flag = 0
    for j in range(len(result) - 1, -1, -1):
        if result[j] <= i:
            result.insert(j + 1, i)
            flag = 1
            break
    if not flag:
        result.insert(0, i)
print(result)