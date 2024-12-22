def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))