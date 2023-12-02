from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
for a in A:
    count[a] += 1

count = dict(sorted(count.items(), reverse=True, key=lambda x:x[0]))
max_xy = []
for k, v in count.items():
    if v >= 2:
        if v >= 4:
            max_xy.append(k)
            max_xy.append(k)
        else:
            max_xy.append(k)
    if len(max_xy) >= 2:
        print(max_xy[0]*max_xy[1])
        exit()

print(0)