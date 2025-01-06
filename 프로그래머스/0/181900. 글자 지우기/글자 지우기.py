def solution(my_string, indices):
    my_arr = list(my_string)
    for i in indices:
        my_arr[i] = ''
    return ''.join(my_arr)