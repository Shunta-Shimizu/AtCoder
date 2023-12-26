n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])

AB = list(sorted(AB, key=lambda x:x[1]))

t = 0
tf = True
for i in range(n):
    t += AB[i][0]
    if t > AB[i][1]:
        tf = False

if tf:
    print("Yes")
else:
    print("No")