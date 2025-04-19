import sys
input = sys.stdin.readline

for x, y in sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda p: (p[1], p[0])):
    print(x, y)