M, N = map(int, input().split())

l = []
for _ in range(M):
    l.append(list(input()))

min_l = []
for i in range(len(l) - 7):
    for j in range(len(l[i]) - 7):
        startW = 0
        startB = 0
        for t in range(i, i + 8):
            if t % 2 == 0:
                c = 'W'
            else:
                c = 'B'
            for q in range(j, j + 8):
                if l[t][q] != c:
                    startW += 1
                else:
                    startB += 1

                if c == 'W':
                    c = 'B'
                else:
                    c = 'W'
        min_l.append(min(startW, startB)) 

print(min(min_l))