n = int(input())
A = list(map(int, input().split()))

tf = [False] * n

for i in range(n):
    if tf[i] == False:
        tf[A[i]-1] = True

ans = []
for i in range(n):
    if not tf[i]:
        ans.append(i+1)

print(len(ans))
print(*ans, sep=" ")
