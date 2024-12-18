def solution(num_list):
    sum1 = sum(num_list[i] for i in range(0, len(num_list), 2))
    sum2 = sum(num_list[i] for i in range(1, len(num_list), 2))
    
    return max(sum1, sum2)