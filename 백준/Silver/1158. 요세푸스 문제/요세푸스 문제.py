import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = [i for i in range(1, N + 1)]

result = []
idx = K - 1

s = set()
while 1:
    if l[idx] not in s:
        result.append(l[idx])
        s.add(l[idx])
        l.pop(idx)

    if not l:
        break
        
    idx = (idx + K - 1) % len(l)

print("<", end="")
print(*result, sep=", ", end="")
print(">")