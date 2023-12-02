from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

a_count = defaultdict(int)
for i in range(n):
    a_count[A[i]] += 1

ans = 0
for ai in range(-200, 201):
    for aj in range(-200, 201):
        ans += (ai-aj)**2 * a_count[ai] * a_count[aj]

print(ans//2)