from functools import lru_cache
n = int(input())

@lru_cache
def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1)+[n]+f(n-1)

ans = f(n)
print(*ans)