def solution(d, budget):
    count = 0
    d.sort()
    for j in d:
        budget -= j
        if budget < 0:
            break
        
        count += 1
    return count