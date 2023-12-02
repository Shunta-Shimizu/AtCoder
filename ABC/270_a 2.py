a, b = map(int, input().split())

ans = bin(a|b)
print(int(ans, 2))

# print(a|b)