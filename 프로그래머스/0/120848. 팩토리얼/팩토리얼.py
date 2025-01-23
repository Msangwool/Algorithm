def solution(n):
    f = 1
    for i in range(1,11):
        f *= i
        if f == n:
            return i
        elif f > n:
            return i - 1
    return 0