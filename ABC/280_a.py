H, W = map(int, input().split())

count = 0
for _ in range(H):
    S = list(input())
    count += S.count("#")

print(count)