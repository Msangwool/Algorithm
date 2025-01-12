def solution(strArr):
    arrLength = [len(s) for s in strArr]
    
    counts = {}
    for l in arrLength:
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1

    return max(counts.values())