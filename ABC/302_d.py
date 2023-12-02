from collections import defaultdict
n, m, d = map(int, input().split())
A = list(map(int, input().split()))
B =list(map(int, input().split()))

AB_dict = defaultdict(str)
for i in range(n):
    A[i] += d
    AB_dict[A[i]] = "A"

B_dict = defaultdict(int)
for i in range(m):
    AB_dict[B[i]] = "B"

AB_dict = dict(sorted(AB_dict.items(), key=lambda x:x[0]))
print(AB_dict)