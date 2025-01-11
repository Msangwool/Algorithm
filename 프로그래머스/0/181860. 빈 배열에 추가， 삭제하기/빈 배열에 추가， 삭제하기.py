def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * (arr[i] * 2))
            continue
        
        for j in range(arr[i]):
            X.pop()
    return X