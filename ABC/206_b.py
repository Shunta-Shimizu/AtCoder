n = int(input())

ans = 0
i = 1
while True:
    ans += i
    if ans >= n:
        break
    i += 1
print(i)