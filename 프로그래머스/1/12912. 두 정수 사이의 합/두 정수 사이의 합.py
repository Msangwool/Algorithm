def solution(a, b):
    return sum(num for num in range(a, b+1)) if a <= b else sum(num for num in range(b, a+1))