n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

a_max = max(A)
b_min = min(B)

# if b_min - a_max <= 0:
#     print(0)
# else:
#     print(b_min - a_max + 1)
print(max(0, b_min - a_max + 1))