import math
import sys

input = sys.stdin.readline

def isPrimeNum(num):
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    i = int(input())

    if i <= 1:
        print(2)
        continue

    while 1:
        if isPrimeNum(i):
            break
        i += 1
    print(i)