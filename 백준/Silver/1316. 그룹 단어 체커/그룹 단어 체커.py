cnt = int(input())
for _ in range(cnt):
    
    t = input()
    target = ''
    dp = []
    for c in t:
        if c == target:
            continue
        
        if c in dp:
            cnt -= 1
            break
            
        target = c
        dp.append(target)

print(cnt)