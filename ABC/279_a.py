S = list(input())

count = 0
for s in S:
    if s == "v":
        count += 1
    elif s == "w":
        count += 2

print(count)