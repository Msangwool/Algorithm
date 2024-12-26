def solution(numLog):
    keys = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    answer = ''
    
    before_num = numLog[0]
    for i in range(1, len(numLog)):
        answer += keys[numLog[i] - before_num]
        before_num = numLog[i]
    return answer