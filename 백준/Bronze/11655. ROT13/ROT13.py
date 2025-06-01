for c in input():
    if c == " " or c.isdigit():
        print(c, end="")
        continue
    
    if c.isupper():
        print(chr(((ord(c) - ord('A') + 13) % 26) + ord('A')), end="")
    else:
        print(chr(((ord(c) - ord('a') + 13) % 26) + ord('a')), end="")