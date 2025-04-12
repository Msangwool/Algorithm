l_x = []
l_y = []

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    l_x.append(x)
    l_y.append(y)

if N <= 1:
    print(0)
else:
    l_x.sort()
    l_y.sort()
    print((l_x[-1] - l_x[0]) * (l_y[-1] - l_y[0]))