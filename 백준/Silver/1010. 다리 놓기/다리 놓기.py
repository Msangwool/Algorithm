import sys
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
            
def nCk(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

for _ in range(int(input())):
    N, M = map(int, input().strip().split())
    
    print(nCk(M, N))