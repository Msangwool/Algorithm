import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
filtered = []
for _ in range(N):
    s = input().strip()
    if len(s) < M:
        continue

    filtered.append(s)

freq = Counter(filtered)

result = sorted(freq.keys(), key=lambda x: (-freq[x], -len(x), x))
print(*result, sep="\n")