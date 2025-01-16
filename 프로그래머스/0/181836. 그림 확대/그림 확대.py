def solution(picture, k):
    answer = []
    for s in picture:
        copyS = ''
        for i in range(len(s)):
            copyS += s[i]*k;
        
        for i in range(k):
            answer.append(copyS)
    return answer