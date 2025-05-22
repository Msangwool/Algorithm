def solution(id_pw, db):
    d = dict()
    for l in db:
        d[l[0]] = l[1]
        
    if id_pw[0] not in d:
        return "fail"
    
    if d[id_pw[0]] != id_pw[1]:
        return "wrong pw"
    
    return "login"