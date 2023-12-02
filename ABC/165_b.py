x = int(input())

ans = 0
money = 100
while True:
    money = money + (money // 100)
    ans += 1
    if money >= x:
        break

print(ans)