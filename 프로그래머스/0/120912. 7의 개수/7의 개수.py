def solution(array):
    c = 0
    for i in array:
        c += str(i).count('7')
    return c