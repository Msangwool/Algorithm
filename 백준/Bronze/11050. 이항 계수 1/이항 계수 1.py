import sys
input = sys.stdin.readline

def factorial_v1(num, cnt):
    result = 1
    for i in range(cnt):
        result *= num
        num -= 1
    return result 

def factorial_v2(num, limit):
    if num < limit:
        return 1
    return num * factorial_v2(num - 1, limit)

N, K = map(int, input().strip().split())

print(factorial_v1(N, K) // factorial_v2(K, 1))