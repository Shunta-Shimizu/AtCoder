a, b, w = map(int, input().split())

ans = set()
for i in range(1, w*1000+1):
    if a*i <= w*1000 <= b*i:
        ans.add(i)

if len(ans) == 0:
    print("UNSATISFIABLE")
else:
    print(min(ans), max(ans))
