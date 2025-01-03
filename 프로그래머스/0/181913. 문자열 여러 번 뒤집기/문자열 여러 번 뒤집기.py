def solution(my_string, queries):
    my_list = list(my_string)
    for query in queries:
        s = query[0]
        e = query[1]

        my_list[s:e+1] = my_list[s:e+1][::-1]
    return ''.join(my_list)