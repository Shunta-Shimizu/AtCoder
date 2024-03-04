n = int(input())
A = list(map(int, input().split()))

now = [0 for _ in range(n)]
for i, a in enumerate(A):
    if i == 0:
        now[i] = a
    else:
        now[i] = now[i-1]+a

ans = abs(min(0, min(now)))
print(now[-1]+ans)