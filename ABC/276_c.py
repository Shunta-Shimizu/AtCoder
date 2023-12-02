import itertools
N = int(input())
#P = list(map(int, input().split()) for _ in range(N))
P = list(map(int, input().split()))
P_sort = sorted(P)
ans_list = list(itertools.permutations(P_sort))

for i in range(len(ans_list)):
    ans_list[i] = list(ans_list[i])

P_idx = ans_list.index(P)
print(*ans_list[P_idx-1], sep=" ")