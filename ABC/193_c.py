import math
n = int(input())

ans = set()
i = 2
while True:
    num = math.pow(n, 1/i) + 10 ** (-10)
    if num < 2:
        break
    else:
        num = int(num)
        # print(num)
        for j in range(2, num+1):
            ans.add(j**i)
        i += 1
# print(ans)
# print(len(ans))
print(n-len(ans))
