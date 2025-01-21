def solution(emergency):
    answer = [0] * len(emergency)
    for i, num in enumerate(sorted(emergency, reverse=True)):
        answer[emergency.index(num)] = i+1
    return answer