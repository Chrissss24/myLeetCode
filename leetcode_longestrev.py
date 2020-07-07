s = "babad"

length = len(s)
result = ""
for i in range(2 * length - 1):
    if i % 2 == 0:
        index = 0
        while(
                i // 2 - index >= 0 and
                i // 2 + index < length and
                s[i // 2 - index] == s[i // 2 + index]
            ):
            temp = s[i // 2 - index : i // 2 + index + 1]
            if len(temp) > len(result):
                result = temp
            index += 1
    elif i % 2 == 1:
        index = 0
        while(
                (i - 1) // 2 - index >= 0 and
                (i + 1) // 2 + index < length and
                s[(i - 1) // 2 - index] == s[(i + 1) // 2 + index]
            ):
            temp = s[(i - 1) // 2 - index : (i + 1) // 2 + index + 1]
            if len(temp) > len(result):
                result = temp
            index += 1
print(result)