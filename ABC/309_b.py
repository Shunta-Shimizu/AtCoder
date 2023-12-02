n = int(input())
A = []
for _ in range(n):
    a = list(input())
    A.append(a)

ans = [["" for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                ans[i][j] = A[i+1][j]
            else:
                ans[i][j] = A[i][j-1]
        elif 0 < i < n-1:
            if j == 0:
                if i < n-1:
                    ans[i][j] = A[i+1][j]
            elif j < n-1:
                ans[i][j] = A[i][j]
            else:
                ans[i][j] = A[i-1][j]
        else:
            if j == n-1:
                ans[i][j] = A[i-1][j]
            else:
                ans[i][j] = A[i][j+1]


# print("-------")
for i in range(n):
    print(*ans[i], sep="")



