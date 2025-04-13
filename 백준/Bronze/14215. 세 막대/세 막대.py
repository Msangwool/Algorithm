l = sorted(list(map(int, input().split())))

if l[0] + l[1] > l[2]:
    print(sum(l))
else:
    print(l[0] + l[1] + (l[0] + l[1] - 1))