n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = []
A.sort()
for i in range(q):
    b = int(input())
    B.append(b)

ans = []
for i in range(q):
    if n == 1:
        a = abs(B[i]-A[0])
    else:
        left = 0
        right = n-1
        while right-left > 1:
            mid = (left+right)//2
            if B[i] < A[mid]:
                right = mid
            elif B[i] > A[mid]:
                left = mid
            else:
                break
        a = min(abs(B[i]-A[left]), abs(B[i]-A[right]), abs(B[i]-A[mid]))
    ans.append(a)

print(*ans, sep="\n")
    