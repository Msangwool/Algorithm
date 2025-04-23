def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

def getGcd(l):
    gcd = l[0]
    for i in range(1, len(l)):
        gcd = GCD(gcd, l[i])
    return gcd

N = int(input())
l = [int(input()) for _ in range(N)]
sub_l = [l[i + 1] - l[i] for i in range(N - 1)]

gcd = getGcd(sub_l)

cnt = 0
for i in range(len(sub_l)):
    cnt += sub_l[i] // gcd - 1

print(cnt)