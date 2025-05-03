import sys
import math
input = sys.stdin.readline

# 에라토스테네스 체
M, N = map(int, input().split())

if M == 1:
    M += 1
    
l = [True for _ in range(N + 1)]

for i in range(2, N + 1):
    if l[i] == False:
        continue
    j = 2
    while i * j <= N:
        l[i * j] = False
        j += 1

for i in range(M, N + 1):
    if l[i]:
        print(i)