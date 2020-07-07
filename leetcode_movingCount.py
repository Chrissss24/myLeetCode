def one(num):
    return num

def two(num):
    return (num // 10) + (num % 10)

def three(num):
    return (num // 100) + (num % 100 // 10) + (num % 10)

mydict = {
    1: one,
    2: two,
    3: three
}

m, n, k = 2, 3, 10

if k == 0:
    print(1)

result = 0
if k <= n - 1:
    temp = k + 1
    for i in range(m):
        result += temp - i
        if temp - i == 1:
            break
else:
    if k - n + 1 <= m:
        result += (k - n + 1) * n
    for i in range(m):
        result += n - i
        if n - i == 1:
            break
print(result)


