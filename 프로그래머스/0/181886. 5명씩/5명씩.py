def solution(names):
    answer = []
    for idx, name in enumerate(names):
        if (idx % 5 == 0):
            answer.append(name)
    return answer