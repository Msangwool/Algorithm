a = int(input())
b = int(input())
c = int(input())
l = len(set({a, b, c}))

if sum([a, b, c]) != 180:
    print('Error')
elif l == 1:
    print('Equilateral')
elif l == 2:
    print('Isosceles')
elif l == 3:
    print('Scalene')