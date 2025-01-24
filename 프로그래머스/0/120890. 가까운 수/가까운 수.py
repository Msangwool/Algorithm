def solution(array, n):
    l = sorted([abs(n - i) for i in array])
    print(l)
    return n - l[0] if n - l[0] in array else n + l[0]