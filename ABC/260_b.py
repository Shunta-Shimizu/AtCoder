n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
N = [i+1 for i in range(n)]

A_sort = sorted(A, reverse=True)
pass_num = []
for i in range(x):
    math_pass = A.index(A_sort[i])
    pass_num.append(math_pass+1)
    A[math_pass] = -1
    B[math_pass] = -1
# print(pass_num)

B_sort = sorted(B, reverse=True)
for j in range(y):
    eng_pass = B.index(B_sort[j])
    pass_num.append(eng_pass+1)
    B[eng_pass] = -1
    A[eng_pass] = -1
# print(pass_num)

for p in pass_num:
    N.remove(p)

rest_num = {}
for num in N:
    score = A[num-1] + B[num-1]
    rest_num[num] = score

rest_num = dict(sorted(rest_num.items(), key=lambda x:x[1], reverse=True))
count = 0
for key in rest_num.keys():
    if count == z:
        break
    pass_num.append(key)
    count += 1
# print(pass_num)
# pass_num = set(pass_num)
# pass_num = list(pass_num)
pass_num.sort()
print(*pass_num, sep="\n")