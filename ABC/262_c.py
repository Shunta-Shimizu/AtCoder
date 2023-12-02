n = int(input())
A = list(map(int, input().split()))

count = 0
count2 = 0
for i in range(n):
    if i+1 == A[i]:
        count += 1
    else:
        j = A[i] - 1
        if A[j] == i+1:
            count2 += 1
            # print(i+1, j+1)

ans = count * (count-1) // 2 + count2 // 2
print(ans)