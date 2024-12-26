def solution(num_list):
    answer = 1
    for num in num_list:
        answer *= num
        
    sumResult = sum(num_list)
    return int(answer < sumResult*sumResult)