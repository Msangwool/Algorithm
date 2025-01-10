def solution(n_str):
    idx = 0
    for i in n_str:
        if i != '0':
            break;
        
        idx += 1
    return n_str[idx:]