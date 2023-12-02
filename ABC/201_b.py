n = int(input())

ST = []
for _ in range(n):
    s, t = map(str, input().split())
    ST.append([s, int(t)])

ST.sort(reverse=True, key=lambda x:x[1])

print(ST[1][0])