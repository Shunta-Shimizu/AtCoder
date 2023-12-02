n = int(input())

name = set()
for _ in range(n):
    s, t = map(str, input().split())
    name.add((s, t))

if len(name) != n:
    print("Yes")
else:
    print("No")