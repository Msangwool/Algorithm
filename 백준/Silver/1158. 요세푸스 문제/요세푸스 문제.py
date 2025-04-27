import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = [i for i in range(1, N + 1)]

result = []
idx = 0

s = set()
while l:
    idx = (idx + K - 1) % len(l)
    
    if l[idx] not in s:
        result.append(l[idx])
        s.add(l[idx])
        l.pop(idx)

print("<", end="")
print(*result, sep=", ", end="")
print(">")