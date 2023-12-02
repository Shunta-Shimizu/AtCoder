n = int(input())
S = list(input())

ans1 = 0
ans2 = 0
for i in range(n):
    if S[i] == "T":
        ans1+= 1
    else:
        ans2 += 1


if ans1 > ans2:
    print("T")
elif ans1 < ans2:
    print("A")
else:
    if S[-1] == "A":
        print("T")
    else:
        print("A")