n = int(input())
A = list(map(int, input().split()))

count = [0 for _ in range(2*n+1)]

for i, a in enumerate(A):
    count[2*i+1] = count[a-1] + 1
    count[2*i+2] = count[a-1] + 1

print(*count, sep="\n")
