N = int(input())
l = [0] * 20000002
for i in map(int, input().split()):
    l[i] += 1
M = int(input())
print(*[l[i] for i in map(int, input().split())])