from collections import defaultdict

n, m ,t = map(int, input().split())
A = list(map(int, input().split()))

add_time = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    add_time[x] = y

now = 1
time = t

while True:
    time -= A[now-1]
    if time <= 0:
        print("No")
        break
    now += 1
    if now == n:
        print("Yes")
        break
    if add_time[now]:
        time += add_time[now]

    
