def solution(rank, attendance):
    rankIdx = {}
    for i in range(len(rank)):
        if attendance[i]:
            rankIdx[rank[i]] = i
            
    sortedRank = sorted(rankIdx)
    a = rankIdx[sortedRank[0]]
    b = rankIdx[sortedRank[1]]
    c = rankIdx[sortedRank[2]]    
    
    return 10000*a + 100*b + c