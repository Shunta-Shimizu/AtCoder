# Python TLE n=10, m=10のとき
# PyPyで提出
import itertools

n , m = map(int, input().split())

# permutations：順列
ans = itertools.permutations([i+1 for i in range(m)], n-1)

for a in ans:
    a_sort = sorted(list(a))
    if a == tuple(a_sort):
        print(*a)