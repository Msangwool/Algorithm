import sys

s = sys.stdin.readline().strip()

parts = s.split('-')

def group_sum(token: str) -> int:
    return sum(map(int, token.split('+')))

answer = group_sum(parts[0])       
for token in parts[1:]:            
    answer -= group_sum(token)

print(answer)
