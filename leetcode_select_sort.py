data = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
result = []

while len(data):
    minNum = data[0]
    for i in range(len(data)):
        if data[i] < minNum:
            minNum = data[i]
    idx = data.index(minNum)
    data.pop(idx)
    result.append(minNum)
print(result)