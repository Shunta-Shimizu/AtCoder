n = int(input())
A = list(map(int, input().split()))

A_set = set(A)
if len(A_set)  == 1:
    print("Yes")
else:
    print("No")