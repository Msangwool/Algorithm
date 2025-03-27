n, x = map(int, input().split())
A = list(map(int, input().split()))
result = []
for i in A:
    if i < x:
        result.append(i)
print(' '.join(map(str, result)))