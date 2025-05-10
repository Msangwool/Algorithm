import sys
input = sys.stdin.readline

def A(N):
    return round(sum(N) / len(N))

def B(N):
    N.sort()
    return N[len(N)//2]

def C(N):
    temp = [0] * 500001
    for i in N:
        temp[i] += 1
    m = max(temp)
    m_list = []
    for i in N:
        if temp[i] == m and i not in m_list:
            m_list.append(i)
            if len(m_list) == 2:
                break
    m_list.sort()
    return m_list[0] if len(m_list) == 1 else m_list[1]

def D(N):
    return max(N) - min(N)

N = []
for _ in range(int(input())):
    N.append(int(input()))

print(A(N))
print(B(N))
print(C(N))
print(D(N))