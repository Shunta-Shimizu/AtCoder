n, x = map(int, input().split())
S = input()

for i in range(n):
    if S[i] == "o":
        x += 1
    else:
        x -= 1
        x = max(0, x)

print(x)