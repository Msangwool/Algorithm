def solution(arr, n):
    startIdx = 0
    if len(arr) % 2 == 0:
        startIdx = 1
    for i in range(startIdx, len(arr), 2):
            arr[i] += n
    return arr