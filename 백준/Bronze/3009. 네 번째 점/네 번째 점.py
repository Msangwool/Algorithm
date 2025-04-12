l_x = []
l_y = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in l_x:
        l_x.remove(x)
    else:
        l_x.append(x)
        
    if y in l_y:
        l_y.remove(y)
    else:
        l_y.append(y)

print(l_x[0], l_y[0])