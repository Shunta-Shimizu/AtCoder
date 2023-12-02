n = int(input())
V = list(map(int, input().split()))

V.sort()
v_mean = V[0]
for i in range(1, n):
    ans = (V[i] + v_mean) / 2
    v_mean = (V[i] + v_mean) / 2

print(ans)