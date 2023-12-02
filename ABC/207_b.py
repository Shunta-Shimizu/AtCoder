a, b, c, d = map(int, input().split())

blue_num = a
red_num = 0

for i in range(a):
    blue_num += b
    red_num += c
    if blue_num <= red_num * d:
        print(i+1)
        exit()

print(-1)