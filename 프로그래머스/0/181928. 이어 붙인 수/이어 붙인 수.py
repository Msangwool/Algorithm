def solution(num_list):
    odd_list = []
    even_list = []
    
    for num in num_list:
        if (num % 2 == 1):
            odd_list.append(str(num))
            continue
        even_list.append(str(num))
    
    return int(''.join(odd_list)) + int(''.join(even_list))