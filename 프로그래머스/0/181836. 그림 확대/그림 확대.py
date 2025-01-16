def solution(picture, k):
    answer = []
    for s in picture:
        copyS = s.replace('.', '.'*k).replace('x', 'x'*k);
        for i in range(k):
            answer.append(copyS)
    return answer