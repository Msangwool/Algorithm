l = []

for _ in range(9):
    l.append(list(map(int, input().split())))
    
m = 0;
x = 0;
y = 0;

for i in range(9):
    for j in range(9):
        if l[i][j] >= m:
            m = l[i][j]
            x, y = i + 1, j + 1

print(m)
print(x, y)