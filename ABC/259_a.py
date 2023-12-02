n, m, x, t, d = map(int, input().split())

age = 0
tall = t - d * x
for _ in range(x):
    if age == m:
        print(tall)
        exit()
    tall += d
    age += 1

if m >= x:
    print(t)
