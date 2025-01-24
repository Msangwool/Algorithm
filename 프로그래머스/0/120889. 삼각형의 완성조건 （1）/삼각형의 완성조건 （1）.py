def solution(sides):
    sides.sort()
    return int(sides[0] + sides[1] <= sides[2]) + 1