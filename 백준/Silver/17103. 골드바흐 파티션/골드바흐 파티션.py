import sys
input = sys.stdin.readline

max = 1000000

l = [True] * (max + 1)
l[0] = l[1] = False

for i in range(2, int(max**0.5) + 1):
    if l[i]:
        for j in range(i*i, max + 1, i):
            l[j] = False

for _ in range(int(input())):
    N = int(input())
    cnt = 0
    for a in range(2, N//2 + 1):
        if l[a] and l[N - a]:
            cnt += 1
    print(cnt)