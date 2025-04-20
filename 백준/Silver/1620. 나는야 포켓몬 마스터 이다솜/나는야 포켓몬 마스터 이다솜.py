import sys
input = sys.stdin.readline

N, M = map(int, input().split())

m = dict()
m_name = dict()
for i in range(N):
    s = input().strip()
    m[i+1] = s
    m_name[s] = i+1

l = []
for _ in range(M):
    target = input().strip()

    if target.isdigit():
        l.append(m[int(target)])
    else:
        l.append(m_name[target])

print(*l, sep="\n")