def solution(n):
    return sum(i for i in range(1,(n//2)+1) if n % i == 0) + n