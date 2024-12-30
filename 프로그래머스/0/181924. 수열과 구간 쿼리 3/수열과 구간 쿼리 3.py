def solution(arr, queries):
    for query in queries:
        changeNum(arr, query[0], query[1])
    return arr

def changeNum(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]