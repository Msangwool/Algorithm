import sys
input = sys.stdin.readline

d = dict()

N, M = map(int, input().strip().split())
for _ in range(N):
    s = input().strip()
    if len(s) < M:
        continue

    if s in d:
        d[s] += 1
    else:
        d[s] = 1

result = []
for key in d.keys():
    result.append((key, d[key]))

result = sorted(result, key=lambda x: (-x[1], -len(x[0]), x[0]))
for t in result:
    print(t[0])