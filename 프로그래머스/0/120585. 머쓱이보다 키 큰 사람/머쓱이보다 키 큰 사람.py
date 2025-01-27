def solution(array, height):
    return sum(int(i > height) for i in array)