key = []
cnt = []

value = input().lower()
for v in value:
    if v not in key:
        key.append(v)
        cnt.append(value.count(v))
       
m = 0
idx = 0
b = False
for i, v in enumerate(cnt):
    if v > m:
        m = v
        idx = i
        b = False
    elif v == m:
        b = True

if b:
    print('?')
else:
    print(key[idx].upper())