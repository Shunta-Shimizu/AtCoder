a, b, c = map(int, input().split())

res = set()
n = a
i = 1
while True:
    n = a*i
    if n % b == c:
        print("YES")
        break
    else:
        if n % b in res:
            print("NO")
            break
        else:
            res.add(n%b)
    i += 1
