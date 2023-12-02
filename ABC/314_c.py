from collections import deque, defaultdict
n, m = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

nums = defaultdict(deque)
for i in range(n):
    nums[C[i]].append(S[i])

for v in nums.values():
    if len(v) == 1:
        continue
    n_l = v.pop()
    v.appendleft(n_l)

ans = ""
for i in range(n):
    ans += nums[C[i]].popleft()

print(ans)
