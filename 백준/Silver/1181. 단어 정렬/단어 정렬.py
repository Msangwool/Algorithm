import sys
input = sys.stdin.readline

l = []
n = int(input())
for _ in range(n):
    s = input().strip()
    if s not in l:
        l.append(s)

l.sort(key=lambda s: (len(s), s))
for s in l:
    print(s)