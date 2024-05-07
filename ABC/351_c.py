n = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(n):
    if len(ans) == 0:
        ans.append(A[i])
    else:
        while len(ans) >= 2:
            if ans[-2] == ans[-1]:
                ans.pop()
                ans[-1] += 1
            else:
                break
4 2
2 3 1 4

    # print(ans)
print(len(ans))
