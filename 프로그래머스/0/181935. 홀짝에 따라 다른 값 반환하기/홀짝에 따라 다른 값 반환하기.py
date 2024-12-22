def solution(n):
    return sum([i*i for i in range(0, n+1, 2)]) if n%2==0 else sum([i for i in range(1, n+1, 2)])