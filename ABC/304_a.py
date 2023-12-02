n = int(input())
SA = []
for _ in range(n):
    s, a = map(str, input().split())
    SA.append(((s, int(a))))


SA2 = sorted(SA, key=lambda x:x[1])
f = SA2[0]
ans1 = SA[SA.index(f):]
ans2 = SA[:SA.index(f)]
ans = ans1 + ans2
for a in ans:
    print(a[0])
