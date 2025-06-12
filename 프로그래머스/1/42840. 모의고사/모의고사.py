def solution(answers):
    super1 = [1, 2, 3, 4, 5]
    super2 = [2, 1, 2, 3, 2, 4, 2, 5]
    super3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    super_cnt = [0, 0, 0]
    
    for i, t in enumerate(answers):
        if super1[i % len(super1)] == t:
            super_cnt[0] += 1
        if super2[i % len(super2)] == t:
            super_cnt[1] += 1
        if super3[i % len(super3)] == t:
            super_cnt[2] += 1
            
    m = max(super_cnt)
    return [i + 1 for i in range(3) if super_cnt[i] == m]