p = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            p[i][j] = 1

area = 0
for i in range(len(p)):
    area += p[i].count(1)

print(area)