n, x, y = map(int, input().split())

red = [0] * (n+1)
blue = [0] * (n+1)

red[n] = 1
for i in range(n, 1, -1):
    red[i-1] += red[i]*1
    blue[i] += red[i]*x

    red[i-1] += blue[i]*1
    blue[i-1] += blue[i]*y

print(blue[1])