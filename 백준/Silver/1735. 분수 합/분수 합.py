def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

A_1, B_1 = map(int, input().split())
A_2, B_2 = map(int, input().split())

lcm = 0
if B_1 > B_2:
    lcm = B_1 * B_2 // GCD(B_1, B_2)
else:
    lcm = B_1 * B_2 // GCD(B_2, B_1)

A = lcm // B_1 * A_1 + lcm // B_2 * A_2


gcd = 0
if A > lcm:
    gcd = GCD(A, lcm)
else:
    gcd = GCD(lcm, A)
    
print(A//gcd, lcm//gcd)