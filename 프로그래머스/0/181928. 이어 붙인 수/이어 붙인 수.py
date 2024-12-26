def solution(num_list):
    odd_list = [str(num) for num in num_list if num % 2 == 1]
    even_list = [str(num) for num in num_list if num % 2 == 0]
        
    return int(''.join(odd_list)) + int(''.join(even_list))