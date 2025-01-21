def solution(numbers, direction):
    answer = [0] * len(numbers)
    
    if direction == 'right':
        for i, num in enumerate(numbers):
            answer[(i + 1) % len(numbers)] = num
        return answer
    
    for i, num in enumerate(numbers):
        if i - 1 < 0:
            answer[len(numbers) - 1] = num
            continue
        
        answer[i - 1] = num
    return answer