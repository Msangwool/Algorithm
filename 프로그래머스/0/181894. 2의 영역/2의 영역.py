def solution(arr):
    startIdx = -1
    endIdx = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            startIdx = i
            break
    
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 2:
            endIdx = i
            break
            
    if startIdx == -1:
        return [-1]
            
    if endIdx == -1:
        return arr[startIdx:]
    
    return arr[startIdx:endIdx+1]