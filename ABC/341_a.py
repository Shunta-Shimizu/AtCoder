n = int(input())
ans = ""
for i in range(n*2+1):
    if i%2 == 0:
        ans += "1"
    else:
        ans += "0"

print(ans)