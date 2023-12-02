n, k, q = map(int, input().split())
point = [k for _ in range(n)]

count = [0 for _ in range(n)]
for _ in range(q):
    a = int(input())
    count[a-1] += 1


for i in range(n):
    point[i] += (count[i]-q)
    if point[i] <= 0:
        print("No")
    else:
        print("Yes")