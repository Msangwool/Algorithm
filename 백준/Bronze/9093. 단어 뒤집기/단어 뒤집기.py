import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(*[''.join(reversed(s)) for s in input().split()])