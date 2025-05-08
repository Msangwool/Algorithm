import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

M = int(input())
C = list(map(int, input().strip().split()))[::-1]

for i in range(N):
    if A[i] == 0:
        C.append(B[i])

print(*C[-1:-M-1:-1])