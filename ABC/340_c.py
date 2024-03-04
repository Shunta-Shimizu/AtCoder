from collections import defaultdict
from functools import lru_cache
n = int(input())

memo = defaultdict(int)
def solve(n):
    if n <= 1:
        return 0
    else:
        if n in memo:
            return memo[n]
        a = solve(n//2)+solve((n+1)//2) + n
        memo[n] = a

        return a

@lru_cache
def f(n):
    if n == 1:
        return 0
    else:
        return f(n//2)+f((n+1)//2)+n

print(f(n))