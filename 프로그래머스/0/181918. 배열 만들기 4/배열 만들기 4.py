def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i = i + 1
            continue
            
        stk.pop()
    return stk