import math

x1, y1, x2, y2 = map(int, input().split())

if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) > 2 * math.sqrt(5):
    print("No")
    exit()
else:
    for i in range(int(x1 - math.sqrt(5))+1, int(x1 + math.sqrt(5))+1):
        for j in range(int(y1 - math.sqrt(5)+1), int(y1 + math.sqrt(5))+1):
                if math.sqrt((i - x1) ** 2 + (j - y1) **2) == math.sqrt(5) and math.sqrt((i - x2) ** 2 + (j - y2) ** 2) == math.sqrt(5):
                    print("Yes")
                    # print(i, j)
                    exit()

print("No")