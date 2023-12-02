n = int(input())
A = list(map(int, input().split()))

A.sort()
a_sum = sum(A)
a_div = a_sum // n
a_mod = a_sum % n

Ans_list = [a_div for _ in range(n)]
for i in range(a_mod):
    Ans_list[i] += 1

Ans_list.sort()
ans = 0
for i in range(n):
    ans += abs(A[i]-Ans_list[i])

print(ans // 2)
