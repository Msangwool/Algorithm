import sys
from collections import deque
input = sys.stdin.readline

d = deque()

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

for i in range(N):
    if A[i] == 0:
        d.appendleft(B[i])

M = int(input())
C = list(map(int, input().strip().split()))

for i in range(M):
    d.append(C[i])
    print(d.popleft(), end=" ")