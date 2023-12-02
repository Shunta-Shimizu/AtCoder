n, k, a = map(int, input().split())
Ans = [i+1 for i in range(n)]
for _ in range(k):
    ans = a % n
    a += 1

print(Ans[ans-1])