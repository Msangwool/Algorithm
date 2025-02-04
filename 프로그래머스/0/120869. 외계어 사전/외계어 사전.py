def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if len(s) != len(spell):
            continue
        
        if not spell-set(s):
            return 1
    return 2