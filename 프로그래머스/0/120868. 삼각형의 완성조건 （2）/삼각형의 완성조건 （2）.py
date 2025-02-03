def solution(sides):
    # 1. n + min(sides) > max(sides) == n > max(sides) - min(sides)
    # 2. sum(sides) > n
    
    # 즉, sum(sides) > n > max(sides) - min(sides)
    return sum(sides) - (max(sides) - min(sides)) - 1