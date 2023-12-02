n , k = map(int, input().split())
S = input()

count = 0
ans = ""
for i in range(n):
    if S[i] == "o":
        count += 1
        if count > k:
            ans +="x"
        else:
            ans += "o"
    else:
        ans += "x"
    
print(ans)