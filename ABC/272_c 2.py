n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

even = []
odd = []
for i in range(n):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])
    if len(even) >= 2 or len(odd) >= 2:
        break

if len(even) < 2 and len(odd) < 2:
    print(-1)
else:
    if sum(even) >= sum(odd):
        print(sum(even))
    else:
        print(sum(odd))