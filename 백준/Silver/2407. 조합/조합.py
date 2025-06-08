def factorial_custom(n, cnt):    
    if cnt <= 1:
        return n
    return n * factorial_custom(n-1, cnt-1)
    
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n, m = map(int, input().split())

print(factorial_custom(n, m) // factorial(m))