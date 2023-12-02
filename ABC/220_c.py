n = int(input())
A = list(map(int, input().split()))
x = int(input())

sum_a = sum(A)
l_a = len(A)

ans = l_a * (x // sum_a)
sum_b = sum_a * (x // sum_a)
for i in range(l_a):
    if  sum_b <= x:
        ans += 1
        sum_b += A[i]
    else:
        break

print(ans)