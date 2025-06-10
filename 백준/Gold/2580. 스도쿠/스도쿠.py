import sys
input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(9)]
tgt = []
for x in range(9):
    for y in range(9):
        if p[x][y] == 0:
            tgt.append((x, y))

def is_valid_x(x, n):
    for y in range(9):
        if p[x][y] == n:
            return False
    return True

def is_valid_y(y, n):
    for x in range(9):
        if p[x][y] == n:
            return False
    return True

def is_valid_box(x, y, n):
    start_x, start_y = (x//3) * 3, (y//3) * 3
    for i in range(3):
        for j in range(3):
            if p[start_x + i][start_y + j] == n:
                return False
    return True

def dfs(cnt):
    if cnt == len(tgt):
        for row in range(9):
            print(*p[row])
        sys.exit(0)

    x = tgt[cnt][0]
    y = tgt[cnt][1]
    for i in range(1, 10):
        if is_valid_x(x, i) and is_valid_y(y, i) and is_valid_box(x, y, i):
            p[x][y] = i
            dfs(cnt + 1)
            p[x][y] = 0

dfs(0)