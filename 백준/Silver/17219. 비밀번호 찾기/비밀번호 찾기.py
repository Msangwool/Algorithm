import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pw = {}

for _ in range(N):
    site, password = input().split()
    pw[site] = password

out = []
for _ in range(M):
    query = input().strip()
    out.append(pw[query])

print("\n".join(out))