n, q = map(int, input().split())
S = input()

count = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        count += x
    else:
        print(S[(x-1)-count%n])

