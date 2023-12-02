n = input()

ans = 0
if len(n) <= 3:
    print(ans)
else:
    i = 3
    num = int(n)
    while i <= len(n):
        if num >= 10 ** (i+1):
            ans += (i // 3) * (10**(i+1)-10**i)
            i += 1
        else:
            ans += (i // 3) * (num-10**i + 1)
            break
    
    print(ans)

# ans = 0
# for _ in range(1000, 1010):
#     ans += 1
# print(ans)