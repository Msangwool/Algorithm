l = [1, 1, 2, 2, 2, 8]
for i, v in enumerate(map(int, input().split())):
    print(l[i] - v, end=" ")