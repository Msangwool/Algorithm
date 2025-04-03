d = dict({
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
})

a1 = 0
a2 = 0
for _ in range(20):
    name, v, g = input().split()
    if g == 'P':
        continue
    
    a1 += float(v) * d[g]
    a2 += float(v)
    
print(a1/a2)