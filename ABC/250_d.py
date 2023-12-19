from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
q = int(input())

count = defaultdict(int)
for i, a in enumerate(A):
    count[a] += 1

ans = sum(A)
for _ in range(q):
    b, c = map(int, input().split())
    ans -= b*count[b]
    ans += c*count[b]
    count[c] += count[b]
    count[b] = 0


    print(ans)