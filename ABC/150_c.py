import itertools
n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

P_sort = sorted(P)
permute_P = list(itertools.permutations(P_sort, n))
print(abs(permute_P.index(tuple(P))-permute_P.index(tuple(Q))))

