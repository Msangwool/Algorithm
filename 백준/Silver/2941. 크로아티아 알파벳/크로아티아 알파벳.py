s = input()
a = dict({'c=':'1', 'c-':'2', 'dz=':'3', 'd-':'4', 'lj':'5', 'nj':'6', 's=':'7', 'z=':'8'})

for i in a.keys():
    s = s.replace(i, a[i])

print(len(s))