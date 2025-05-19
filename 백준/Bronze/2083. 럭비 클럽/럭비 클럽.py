while 1:
    query = input()
    if query == '# 0 0':
        break
    name, age, weight = query.split()
    
    if int(age) > 17 or int(weight) >= 80:
        print(name + ' Senior')
    else:
        print(name + ' Junior')