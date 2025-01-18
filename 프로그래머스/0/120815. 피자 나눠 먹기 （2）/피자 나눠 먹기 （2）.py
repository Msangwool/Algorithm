def solution(n):    
    answer = 0
    if n % 6 == 0:
        return n//6
    
    # 최소 공배수 
    # |두 수의 곱| // 최대 공약수
    
    # 최대 공약수
    GCD = 0
    if n > 6:
        GCD = max([i for i in range(1, n+1) if 6%i==0 and n%i==0])
    else:
        GCD = max([i for i in range(1, 7) if n%i==0 and 6%i==0])
        
    return (abs(n*6)//GCD)//6