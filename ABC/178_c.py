n = int(input())

mod = 10**9+7
ans = 0
if n >= 2:
    ans = 1
    two = 1
    nice = 1
    both = 1
    for i in range(n):
        ans *= 10
        two *= 9
        nice *= 9
        both *= 8

        ans %= mod
        two %= mod
        nice %= mod
        both %= mod
    
    ans -= (two+nice-both)

print(ans%mod)