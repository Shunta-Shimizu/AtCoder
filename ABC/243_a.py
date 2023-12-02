v, a, b, c = map(int, input().split())

count = 0
while True:
    if count % 3 == 0:
        if v < a:
            print("F")
            break
        v -= a
    elif count % 3 == 1:
        if v < b:
            print("M")
            break
        v -= b
    elif count % 3 == 2:
        if v < c:
            print("T")
            break
        v -= c
    count += 1
        



