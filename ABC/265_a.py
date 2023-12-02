x, y, n = map(int, input().split())

y_num = n // 3
x_num = n - y_num * 3

if x * x_num + y * y_num >= x * n:
    print(x * n)
else:
    print(x * x_num + y * y_num)