import sys
import math
input = sys.stdin.readline

# 에라토스테네스 체
M, N = map(int, input().split())

if M == 1:
    M += 1
    
l = [True for _ in range(N + 1)]

for i in range(2, math.isqrt(N) + 1):
    if l[i]:
        for j in range(i * i, N + 1, i):
            l[j] = False

for i in range(M, N + 1):
    if l[i]:
        print(i)