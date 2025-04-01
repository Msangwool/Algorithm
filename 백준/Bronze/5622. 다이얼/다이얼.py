dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
m = {}
for i in range(len(dial)):
    for c in dial[i]:
        m[c] = i + 3

min_time = 0
for c in input():
    min_time += m[c]

print(min_time)