from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

same_res = defaultdict(int)
for i in range(n):
    a_res = A[i] % 200 
    same_res[a_res] += 1

ans = 0
for k, v in same_res.items():
    ans += (v*(v - 1))//2

print(ans)