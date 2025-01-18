def solution(my_string, n):
    for s in set(my_string):
        my_string = my_string.replace(s, s*n)
    return my_string