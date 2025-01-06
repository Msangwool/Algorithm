def solution(arr, intervals):
    answer = []
    for interval in intervals:
        a = interval[0]
        b = interval[1] + 1
        
        answer += arr[a:b]
    return answer