m = int(input())
D = list(map(int, input().split()))

ans = (sum(D)+1) // 2
a = 0
b = 0
if m == 1:
    print(1, ans)
else:
    for i in range(m):
        a += 1
        b = 0
        for j in range(D[i]):
            ans -= 1
            b += 1
            if ans == 0:
                print(a, b)
                exit()
