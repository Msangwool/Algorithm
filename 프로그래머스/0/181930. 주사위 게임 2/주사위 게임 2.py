def solution(a, b, c):
    
    if (a == b and b == c):
        return sum(a, b, c) * squareSum(a, b, c) * cubeSum(a, b, c)
    
    if (a != b and b != c and a != c):
        return sum(a, b, c)
        
    return sum(a, b, c) * squareSum(a, b, c)

def sum(a, b, c):
    return a + b + c

def squareSum(a, b, c):
    return a*a + b*b + c*c

def cubeSum(a, b, c):
    return a*a*a + b*b*b + c*c*c