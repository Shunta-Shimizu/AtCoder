import bisect
n, q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
r_sum = [0 for _ in range(n)]
for i, r in enumerate(R):
    if i == 0:
        r_sum[i] = r
    else:
        r_sum[i] = r_sum[i-1]+r

for _ in range(q):
    x = int(input())
    ans = bisect.bisect_right(r_sum, x)
    print(ans)
