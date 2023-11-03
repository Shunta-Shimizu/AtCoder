n = int(input())
a, b, c = map(int, input().split())

coins = [a, b, c]
coins.sort()
a = coins[0]
b = coins[1]
c = coins[2]

ans = 10**8
for i in range(n//c, -1, -1):
    for j in range((n-c*i)//b, -1, -1):
        if n-c*i-b*j >= 0:
            if (n-c*i-b*j) % a == 0:
                k = (n-c*i-b*j) // a
                ans = min(ans, i+j+k)
        
print(ans)