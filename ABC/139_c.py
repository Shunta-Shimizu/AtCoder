n = int(input())
H = list(map(int, input().split()))

ans = set()
count = 0
for i in range(n-1):
    if H[i] >= H[i+1]:
        count += 1
    else:
        ans.add(count)
        count = 0

ans.add(count)
print(max(ans))