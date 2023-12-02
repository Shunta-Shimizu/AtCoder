from collections import defaultdict
n = int(input())
A = []
switch = defaultdict(int)
for i in range(n):
    a = int(input())
    switch[i] = a
    A.append(a)

count = 0
on = 1
while count <= n:
    count += 1
    if switch[on-1] == 2:
        print(count)
        exit()
    on = switch[on-1]

print(-1)