n, x = map(int, input().split())

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""
for i in range(26):
    ans += abc[i] * n 

print(ans[x-1])