def solution(n):
    answer = 1
    m = n//2
    
    if n % 2 == 0:
        answer += 1
        m -= 1
    
    for i in range(1, m + 1):
        answer += mCn(n - i, i)
        
    return answer % 1234567

def mCn(m, n):
    return factorial_v2(m, n) // factorial(n)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_v2(n, cnt):
    if cnt == 1:
        return n
    return n * factorial_v2(n - 1, cnt - 1)