import sys

input = sys.stdin.readline

l = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    l.append((x, y))

l.sort(key=lambda x: (x[0], x[1]))
for t in l:
    print(t[0], t[1])