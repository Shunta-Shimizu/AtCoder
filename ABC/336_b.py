n = int(input())

m = list(bin(n)[3:])
ans = 0
for i in range(len(m)):
    if m[-(i+1)] == "0":
        ans += 1
    else:
        break
print(ans)