import itertools
n = int(input())

ans = list(itertools.product(["a", "b", "c"], repeat=n))
# print(len(ans))
for a in ans:
    print(*list(a), sep="")