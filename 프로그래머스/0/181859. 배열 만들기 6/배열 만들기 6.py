def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
            continue
        
        stk.append(arr[i])
    return stk or [-1]