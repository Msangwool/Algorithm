def solution(n, m):
    gcd = 0
    if n > m:
        gcd = GCD(n, m)
    else:
        gcd = GCD(m, n)
    return [gcd, n*m//gcd]

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a