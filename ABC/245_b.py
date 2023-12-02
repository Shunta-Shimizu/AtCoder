n = int(input())
A = set(map(int, input().split()))

A_set_sort = sorted(list(A))
ans = -1
for i in range(len(A_set_sort)):
    if i == A_set_sort[i]:
        continue
    else:
        ans = i
        break

if ans == -1:
    ans = A_set_sort[-1] + 1
print(ans)