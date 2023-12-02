a, b = map(int, input().split())

ans1 = ""
ans2 = ""
for i in range(b):
    ans1 += str(a)

for i in range(a):
    ans2 += str(b)

if ans1 <= ans2:
    print(ans1)
else:
    print(ans2)