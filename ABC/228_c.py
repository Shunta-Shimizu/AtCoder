n, k = map(int, input().split())

Point = []
for i in range(n):
    P = list(map(int, input().split()))
    Point.append(sum(P))

Point_sort = sorted(Point, reverse=True)
boader = Point_sort[k-1]

for i in range(n):
    if Point[i] + 300 >= boader:
        print("Yes")
    else:
        print("No")
