S = list(input())

n = len(S)

l = 0
r = n - 1

while l < r and S[l] == "a" and S[r] == "a":
    l += 1
    r -= 1

while l < r and S[r] == "a":
    r -= 1
while l < r and S[l] == S[r]:
    l += 1
    r -= 1

if l >= r:
    print("Yes")
else:
    print("No")