def solution(n, k):
    k -= n//10
    return n*12000 + k*2000 if k > 0 else n*12000