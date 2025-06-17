def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

for _ in range(int(input())):
    l = list(map(int, input().split()))
    n = l[0]
    tgt = l[1:]
    
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            result += GCD(tgt[i], tgt[j]) if tgt[i] > tgt[j] else GCD(tgt[j], tgt[i])
    print(result)