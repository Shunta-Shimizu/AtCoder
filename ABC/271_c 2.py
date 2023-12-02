n = int(input())
A = set(map(int, input().split()))

num = 0
while n >= 0:
    if num + 1 in A:
        n -= 1
    else:
        n -= 2
    num += 1

print(num-1)