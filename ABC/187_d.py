n = int(input())

AB = []
sum1 = 0
sum2 = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum1 += a
    # sum2 += b
    AB.append([a, b, 2*a+b])

ans = 0
AB = sorted(AB, key=lambda x:x[2], reverse=True)
for a, b, ab in AB:
    sum2 += ab
    ans += 1
    if sum2 > sum1:
        break
    
print(ans)