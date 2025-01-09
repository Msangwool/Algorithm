def solution(arr1, arr2):
    if (len(arr1) != len(arr2)):
        return 1 if len(arr1) > len(arr2) else -1
    
    sumArr1 = sum(num for num in arr1)
    sumArr2 = sum(num for num in arr2)
    
    if arr1 == arr2 or sumArr1 == sumArr2:
        return 0
    
    if sumArr1 > sumArr2:
        return 1
    return -1