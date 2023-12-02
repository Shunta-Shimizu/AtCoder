N = int(input())
A = list(map(int, input().split()))

odd =[]
even = []
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

odd.sort()
even.sort()

sum_max1 = -1
sum_max2 = -1

if len(odd) >= 2:
    sum_max1 = odd[-2] + odd[-1]
if len(even) >= 2:
    sum_max2 = even[-2] + even[-1]

if sum_max1 >= sum_max2:
    print(sum_max1)
else:
    print(sum_max2)