l = list(map(int, input().split()))

s = set(l)

if len(s) == 1:
    print(10000 + l[0]*1000)
elif len(s) == 3:
    print(max(l)*100)
else:
    for i in s:
        if l.count(i) == 2:
            print(1000 + i*100)
            break