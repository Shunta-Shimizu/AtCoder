import itertools 

S, k = map(str, input().split())

k = int(k)
ans = set(itertools.permutations(S, len(S)))

print(*sorted(ans)[k-1], sep="")
