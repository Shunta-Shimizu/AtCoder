from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

mod46_a = defaultdict(int)
mod46_b = defaultdict(int)
mod46_c = defaultdict(int)

for i in range(n):
    mod46_a[A[i]%46] += 1
    mod46_b[B[i]%46] += 1
    mod46_c[C[i]%46] += 1

ans = 0
for ka, va in mod46_a.items():
    for kb, vb in mod46_b.items():
        for kc, vc in mod46_c.items():
            if (ka+kb+kc)%46 == 0:
                ans += va*vb*vc

print(ans)