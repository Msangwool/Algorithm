def solution(num_list):
    num_list = [num%2 for num in num_list]
    return [num_list.count(0), num_list.count(1)]