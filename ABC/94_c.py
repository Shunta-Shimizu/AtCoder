from collections import deque, defaultdict
n = int(input())
X = list(map(int, input().split()))

X_sort = sorted(X)
nums = defaultdict(deque)
for i in range(n):
    nums[X_sort[i]].append(i)

median1_i = n//2
median2_i = n//2-1
for x in X:
    num = nums[x].popleft()
    if num < median1_i:
        print(X_sort[median1_i])
    else:
        print(X_sort[median2_i])