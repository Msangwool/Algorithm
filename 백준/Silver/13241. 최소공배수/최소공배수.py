import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

A, B = map(int, input().split())
if A > B:
    print(A*B//gcd(A, B))
else:
    print(A*B//gcd(B, A))