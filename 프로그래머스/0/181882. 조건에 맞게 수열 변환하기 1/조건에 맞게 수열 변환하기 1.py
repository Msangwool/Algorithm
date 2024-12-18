def solution(arr):
    return [
        num/2 if isMoreThen50(num) and not isOdd(num) 
        else num*2 if not isMoreThen50(num) and isOdd(num) 
        else num for num in arr]

def isMoreThen50(num):
    return num >= 50

def isOdd(num):
    return num % 2 == 1