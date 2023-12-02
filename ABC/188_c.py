from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

Win = defaultdict(int)
for i in range(2**n):
    Win[i] = 0

iter_n = n
key = list(Win.keys())
for i in range(n):
    for j in range(0, int(2**iter_n), 2):
        if A[key[j]] > A[key[j+1]]:
            Win[key[j]] -= 1
        elif A[key[j]] < A[key[j+1]]:
            Win[key[j+1]] -= 1
    Win = dict(sorted(Win.items(), key=lambda x:x[1]))
    key = list(Win.keys())
    # print(Win)

print(key[1]+1)