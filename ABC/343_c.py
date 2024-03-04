n = int(input())

ans = 0
for i in range(10**6):
    if i**3 > n:
        break
    else:
        if list(str(i**3)) == list(str(i**3))[::-1]:
            ans = i**3

print(ans)