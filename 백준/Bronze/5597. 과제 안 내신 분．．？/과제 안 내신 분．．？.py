l = [i+1 for i in range(30)]

for _ in range(28):
    l[int(input()) - 1] = 0

for i in [j for j in l if j != 0]:
    print(i)