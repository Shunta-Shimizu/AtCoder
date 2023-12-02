n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(n):
    if B[i] in A:
        A.remove(B[i])
        count += 1
        if count == m:
            print("Yes")
            break
    else:
        print("No")
        break
