P = list(map(int, input().split()))

ABC = "abcdefghijklmnopqrstuvwxyz"
ans = ""

for p in P:
    ans += ABC[p-1]

print(ans)