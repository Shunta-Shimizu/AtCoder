a, b = map(int, input().split())

ans = 0
while a != b and a > 0 and b > 0:
    if a > b:
        if b == 1:
            ans += a-1
            break
        else:
            if a % b == 0:
                ans += a//b - 1
            else:
                ans += a//b
            a %= b
    elif a < b:
        if a == 1:
            ans += b-1
            break
        else:
            if b % a == 0:
                ans += b//a - 1
            else:
                ans += b//a
            b %= a
    
print(ans)