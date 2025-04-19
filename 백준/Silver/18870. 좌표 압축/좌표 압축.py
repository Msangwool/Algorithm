import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

d = dict()
for i, num in enumerate(sorted(list(set(l)))):
    d[num] = i

print(*[d[num] for num in l])