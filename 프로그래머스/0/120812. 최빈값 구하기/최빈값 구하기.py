def solution(array):
#     answer = 0
#     d = {}
#     for i in array:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
    
    
#     maxValue = max(d.values())
#     if list(d.values()).count(maxValue) > 1:
#         return -1
    
#     for i, v in d.items():
#         if v == maxValue:
#             answer = i
#             break
            
#     return answer
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1