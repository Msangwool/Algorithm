import sys
import math
input = sys.stdin.readline

def isPrimeNum(num):
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())

if M == 1:
    M += 1

for i in range(M, N + 1):
    if isPrimeNum(i):
        print(i)