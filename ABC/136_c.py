n = int(input())
H = list(map(int, input().split()))

for i in range(n-2, 0, -1):
    if H[i] > H[i+1]+1:
        print("No")
        exit()
    elif H[i] == H[i+1]+1:
        H[i] -= 1

print("Yes")


