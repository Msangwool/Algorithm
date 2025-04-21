import sys
input = sys.stdin.readline

group = set()
s = input().strip()
for i in range(1, len(s)+1):
    for j in range(len(s) + 1 - i):
        group.add(''.join(s[j:j+i]))
print(len(group))