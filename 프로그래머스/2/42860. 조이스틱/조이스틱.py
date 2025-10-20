def solution(name):
    n = len(name)
    total = sum(min(ord(c)-ord('A'), ord('Z')-ord(c)+1) for c in name)

    move = n - 1  
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        move = min(move, i*2 + (n - next_idx))
        move = min(move, (n - next_idx)*2 + i)

    return total + move
