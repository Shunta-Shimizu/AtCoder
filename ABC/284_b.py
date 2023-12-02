t = int(input())

odd_num = []
for _ in range(t):
    n = int(input())
    test = list(map(int, input().split()))
    odd_count = 0
    even = 0
    for t in test:
        if t % 2 != 0:
            odd_count += 1
    odd_num.append(odd_count)

print(*odd_num, sep="\n")