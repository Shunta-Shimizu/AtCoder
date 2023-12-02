N = int(input())
A_org = list(map(int, input().split()))

A_org.sort()
A = list(set(A_org))


#K = [0] * N
# for a in A_org:
#     num = len(A) - (A.index(a)+1)
#     K[num] += 1
# print(*K_dict, sep="\n")

A_dict = {}
for a in A_org:
    if a in A_dict:
        A_dict[a] += 1
    else:
        A_dict[a] = 1

ans = list(A_dict.items())

N_set = len(A)
for i in range(N):
    if i >= N_set:
        print(0)
    else:
        print(ans[N_set-i-1][1])