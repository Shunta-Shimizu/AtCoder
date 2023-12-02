n = int(input())
P = list(map(int, input().split()))

count = 1
i = n
while P[i-2] != 1:
    parent = P[i-2]
    i = parent
    count += 1

print(count)