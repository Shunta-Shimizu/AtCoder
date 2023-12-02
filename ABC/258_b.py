n = int(input())

Grid = []
for _ in range(n):
    A = list(input())
    Grid.append(A)

def calc(g, r, m_x, m_y):
    result = ""
    for i in range(n):
        result += Grid[(g+m_x*i)%n][(r+m_y*i)%n]
    
    result = int(result)
    
    return result

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, calc(i, j, 1, 0))
        ans = max(ans, calc(i, j, 0, 1))
        ans = max(ans, calc(i, j, -1, 0))
        ans = max(ans, calc(i, j, 0, -1))
        ans = max(ans, calc(i, j, 1, -1))
        ans = max(ans, calc(i, j, -1, 1))
        ans = max(ans, calc(i, j, 1, 1))
        ans = max(ans, calc(i, j, -1, -1))

print(ans)




        
            





