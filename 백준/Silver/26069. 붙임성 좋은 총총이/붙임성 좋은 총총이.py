import sys
input = sys.stdin.readline

s = set({'ChongChong'})
for _ in range(int(input())):
    a, b = input().strip().split()
    if a in s:
        s.add(b)
    elif b in s:
        s.add(a)

print(len(s))