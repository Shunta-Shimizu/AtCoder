n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

Ans = []
for _ in range(q):
    x = int(input())
    if x > A[-1]:
        Ans.append(0)
        continue
    else:
        left = -1
        right = n-1
        while 1 < (right - left):
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid
            elif A[mid] >= x:
                right = mid
        # print(left, right)

        Ans.append(n - right)

print(*Ans, sep="\n")



    
