a, b = map(str, input().split())

a = int(a)
b1 = int(b.split(".")[0])
b2 = int(b.split(".")[1])

ans = a * (b1*100 + b2) // 100
print(ans)