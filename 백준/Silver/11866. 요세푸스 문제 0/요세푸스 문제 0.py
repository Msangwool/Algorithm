import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())
q = deque(range(1, N + 1))

output = []
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    output.append(q.popleft())

print("<" + ', '.join(map(str, output)) + ">")