import math
import sys
input = sys.stdin.readline

while 1:
    t = int(input())

    if t == 0:
        break

    if t == 1:
        print(1)
        continue

    n = 2*t
    l = [1 for i in range(n + 1)]

    for i in range(2, math.isqrt(n) + 1):
        if l[i] == 1:
            for j in range(i * i, n + 1, i):
                l[j] = 0

    print(sum(l[t + 1:]))