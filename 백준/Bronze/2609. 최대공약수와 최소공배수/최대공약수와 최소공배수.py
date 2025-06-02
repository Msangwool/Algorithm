def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

A, B = map(int, input().split())
if A > B:
    gcd = GCD(A, B)
else:
    gcd = GCD(B, A)

lcm = (A * B) // gcd

print(gcd)
print(lcm)