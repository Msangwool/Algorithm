import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

M = int(input())
C = deque(map(int, input().strip().split()))

for i in range(N):
    if A[i] == 0:
        C.appendleft(B[i])

print(*list(C)[:M])