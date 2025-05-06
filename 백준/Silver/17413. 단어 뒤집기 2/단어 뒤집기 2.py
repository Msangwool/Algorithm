import sys
input = sys.stdin.readline

str = input().strip()

output = []

targetIdx = str.find("<")
i = 0
while targetIdx != -1:
    temp = str[:targetIdx].split(" ")
    for i in range(len(temp)):
        temp[i] = temp[i][::-1]

    output.append(" ".join(temp))

    nextIdx = str.find(">") + 1
    output.append(str[targetIdx:nextIdx])

    str = str[nextIdx:]
    targetIdx = str.find("<")

temp = str.split(" ")
for i in range(len(temp)):
    temp[i] = temp[i][::-1]

output.append(" ".join(temp))
print(''.join(output))