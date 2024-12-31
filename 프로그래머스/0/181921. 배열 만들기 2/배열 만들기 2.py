def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if i % 5 == 0 and isOnly0And5(i):
            answer.append(i)
    sorted(answer) if answer else answer.append(-1)
    return answer

def isOnly0And5(number):
    number_str = str(number)
    return all(digit in {'0', '5'} for digit in number_str)