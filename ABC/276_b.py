N, M = map(int, input().split())

ans_list = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    ans_list[A-1].append(B)
    ans_list[B-1].append(A)

for ans in ans_list:
    ans.sort()
    print(len(ans), *ans, sep=" ")

# AB_list = []

# for _ in range(M):
#     AB = list(map(int, input().split()))
#     AB_list.append(AB)


# for i in range(1, N+1):
#     d = 0
#     ans = []
#     for j in range(M):
#         if i == AB_list[j][0]:
#             d += 1
#             ans.append(AB_list[j][1])
#         elif i == AB_list[j][1]:
#             d += 1
#             ans.append(AB_list[j][0])
#     ans.sort()
#     print(d, *ans, sep=" ")