H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
else:
    print((H+23)%24, M+15)