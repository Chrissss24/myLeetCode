import re

mystr = "100[leetcode]"

stack = []
m = 0
string = ""

for i in mystr:
    if i == "[":
        stack.append([m, string])
        m = 0
        string = ""
    elif i == "]":
        m1, string1 = stack.pop()
        string = string1 + m1 * string
    elif i >= "0" and i <= "9":
        m = m * 10 + int(i)
    else:
        string += i

print(string)