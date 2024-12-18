def solution(strArr):
    for i, str in enumerate(strArr):
        if (i % 2 == 1):
            strArr[i] = str.upper()
            continue
        
        strArr[i] = str.lower()
    return strArr