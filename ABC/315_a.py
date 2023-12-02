S = input()

l = ["a", "e", "i", "o", "u"]
ans = ""
for s in S:
    if s not in l:
        ans += s

print(ans)