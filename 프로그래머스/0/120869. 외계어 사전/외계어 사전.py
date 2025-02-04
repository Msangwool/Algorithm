def solution(spell, dic):
    for s in dic:
        if len(s) != len(spell):
            continue
        
        b = True
        for i in spell:
            if spell.count(i) != s.count(i):
                b = False
                break
        
        if b:
            return 1
    return 2