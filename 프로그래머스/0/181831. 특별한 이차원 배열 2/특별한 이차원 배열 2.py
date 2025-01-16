def solution(arr):
    answer = 0
    for i in range(len(arr)//2 + 1):
        for j in range(len(arr[i])//2 + 1):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1