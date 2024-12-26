def solution(numLog):
    keys = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    answer = ''
    
    for i in range(1, len(numLog)):
        answer += keys[numLog[i] - numLog[i - 1]]
    return answer