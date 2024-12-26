def solution(num_list):
    num_len = len(num_list)
    if num_list[num_len - 1] > num_list[num_len - 2]:
        num_list.append(num_list[num_len - 1] - num_list[num_len - 2])
        return num_list
    
    num_list.append(num_list[num_len - 1] * 2)
    return num_list