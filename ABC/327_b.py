b = int(input())

for i in range(1, 20):
    if i**i == b:
        print(i)
        exit()

print(-1)