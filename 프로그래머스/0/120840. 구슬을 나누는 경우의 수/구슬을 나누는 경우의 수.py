def solution(balls, share):
    parent = 1
    child = 1
    for i in range(share):
        parent *= (balls-i)
        child *= (share-i)
    return parent//child