from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

rate = defaultdict(int)
over = 0
for a in A:
    if 1 <= a <= 399:
        rate[399] += 1
    elif 400 <= a <= 799:
        rate[799] += 1
    elif 800 <= a <= 1199:
        rate[1199] += 1
    elif 1200 <= a <= 1599:
        rate[1599] += 1
    elif 1600 <= a <= 1999:
        rate[1999] += 1
    elif 2000 <= a <= 2399:
        rate[2399] += 1
    elif 2400 <= a <= 2799:
        rate[2799] += 1
    elif 2800 <= a <= 3199:
        rate[3199] += 1
    elif a >= 3200:
        rate[3200] += 1
        over +=1

min_count = 0
tmp = 0
if over == n:
    min_count = 1
    print(min_count, n)
    exit()
for k, v in rate.items():
    if k < 3200 and v >= 1:
        min_count += 1
    elif k >= 3200 and v >= 1:
        tmp = v

print(min_count, min_count+tmp)

