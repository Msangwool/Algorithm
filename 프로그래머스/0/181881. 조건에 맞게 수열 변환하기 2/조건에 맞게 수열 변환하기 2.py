def solution(arr):
    x = 0
    while True:
        arrX = arr
        arr = [i//2 if i>=50 and i%2==0 else i*2+1 if i<50 and i%2==1 else i for i in arr]
        if arr == arrX:
            break
        x+=1
    return x