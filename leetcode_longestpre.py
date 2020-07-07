a = ["ddd","dddecar","ddd"]
len1 = len(a[0])
short = a[0]
for string in a:
    length = len(string)
    if length < len1:
        short = string
index = 0
result = short[0]
while index < len(short):
    for string in a:
        if result != string[:index+1] and index == 0:
            print("")
            index = 10000
            break
        elif result != string[:index+1] and index > 0:
            print(result[:index])
            index = 10000
            break

    index += 1
    result = short[:index + 1]
print("final result : "+result[:index])

