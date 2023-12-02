n = int(input())
P = list(map(int, input().split()))

# 順列Pの次の順列を求める関数
def next_perm(P, n):
    i = n - 2
    while i >= 0 and P[i] >= P[i+1]:
        i -= 1
    
    j = n - 1
    while P[i] >= P[j]:
        j -= 1
    
    tmp =  P[i]
    P[i] = P[j]
    P[j] = tmp

    i += 1
    j = n - 1
    while i < j:
        tmp = P[i]
        P[i] = P[j]
        P[j] = tmp
        i += 1
        j -= 1
    
    return P

# 順列Pの一つ前の順列を求める処理
# for i in range(n):
#     P[i] = n + 1 - P[i]

# ans = next_perm(P, n)
# for i in range(n):
#     ans[i] = n + 1 - ans[i]

# print(*ans)

print(*next_perm(P, n))