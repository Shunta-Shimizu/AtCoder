w, h, x, y = map(int, input().split())

ans = w*h/2
if x*2 == w and y*2 == h:
    print(ans, 1)
else:
    print(ans, 0)
