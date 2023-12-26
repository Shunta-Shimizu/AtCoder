a, m, l, r = map(int, input().split())

l -= a
r -= a
ans = r//m -(l-1)//m
print(ans)