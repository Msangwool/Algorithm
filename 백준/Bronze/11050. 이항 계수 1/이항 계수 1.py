import sys
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

N, K = map(int, input().strip().split())

print(factorial(N) // (factorial(N - K) * factorial(K)))