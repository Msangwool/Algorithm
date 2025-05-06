import sys
input = sys.stdin.readline

s = input().strip()

output = []

targetIdx = s.find("<")
i = 0
while targetIdx != -1:
    temp = s[:targetIdx].split(" ")
    for i in range(len(temp)):
        temp[i] = temp[i][::-1]

    output.append(" ".join(temp))

    nextIdx = s.find(">") + 1
    output.append(s[targetIdx:nextIdx])

    s = s[nextIdx:]
    targetIdx = s.find("<")

temp = s.split(" ")
for i in range(len(temp)):
    temp[i] = temp[i][::-1]

output.append(" ".join(temp))
print(''.join(output))