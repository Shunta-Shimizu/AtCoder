h, w = map(int, input().split())

C = []
for _ in range(h):
    C.append(list(map(str, input())))

C = list(zip(*C))

count_l = []
for i in range(w):
    count = 0
    count_l.append(C[i].count("#"))

print(*count_l, sep=" ")