N, M = map(int, input().split())

paper = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            paper[x][y] += 1

count = 0
for x in range(1, 101):
    for y in range(1, 101):
        if paper[x][y] > M:
            count += 1

print(count)