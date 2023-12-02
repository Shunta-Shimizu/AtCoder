# import itertools

# n, w = map(int, input().split())
# A = list(map(int, input().split()))

# A.append(0)
# ans = set()

# for i in range(n):
#     if A[i] <= w:
#         ans.add(A[i])

# if n == 1:
#     print(len(ans))
#     exit()

# num_pair = list(itertools.combinations(A, 3))
# for j in range(len(num_pair)):
#     num = num_pair[j][0] + num_pair[j][1] + num_pair[j][2]
#     if num <= w:
#         ans.add(num)

# print(len(ans))

n, w = map(int, input().split())
A = list(map(int, input().split()))

tf = [False] * w
ans = 0
for i in range(n):
    if A[i] <= w and not tf[A[i]-1]:
        tf[A[i]-1] = True
        ans += 1

for i in range(n):
    for j in range(i+1, n):
        num = A[i] + A[j]
        if num <= w and not tf[num-1]:
            tf[num-1] = True
            ans += 1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num2 = A[i] + A[j] + A[k]
            if num2 <= w and not tf[num2-1]:
                tf[num2-1] = True
                ans += 1

print(ans)

