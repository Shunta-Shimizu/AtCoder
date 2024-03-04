n = int(input())

mod = 998244353
m = 1
ans = 0
str_n = str(n)
while True:
    if m == len(str_n):
        c1 = 1+(n-10**(m-1)+1)
        c2 = 1+(n-10**(m-1)+1)-1
        ans += c1*c2//2
        ans %= mod
        break
    else:
        if m == 1:
            c1 = 1+(10**m-1)
            c2 = 1+(10**m-1)-1
        else:
            c1 = 1+(10**m-10**(m-1))
            c2 = 1+(10**m-10**(m-1))-1
        ans  += c1*c2//2
        ans %= mod
        m += 1

print(ans)
