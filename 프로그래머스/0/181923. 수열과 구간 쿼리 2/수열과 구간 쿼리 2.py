def solution(arr, queries):
    answer = []
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        answer.append(safeMin([num for num in arr[s:e + 1:] if num > k]))
    return answer

def safeMin(arr):
    return min(arr) if arr else -1