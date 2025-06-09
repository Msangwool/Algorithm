import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def count(N, t):
    if N < t:
        return 0
    
    count = 0
    while N >= t:
        count += N//t
        N = N//t
    return count

cnt_2 = count(n, 2) - count(n-m, 2) - count(m, 2)
cnt_5 = count(n, 5) - count(n-m, 5) - count(m, 5)
print(min(cnt_2, cnt_5))
