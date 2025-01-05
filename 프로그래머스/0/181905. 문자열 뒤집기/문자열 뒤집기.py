def solution(my_string, s, e):
    my_arr = list(my_string)
    my_arr[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_arr)