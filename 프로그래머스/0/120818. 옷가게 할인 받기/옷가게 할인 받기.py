def solution(price):
    if price >= 500000:
        return price * 4 / 5
    
    if price >= 300000:
        return price * 9 / 10
    
    if price >= 100000:
        return int(price * 19 / 20)
    return price