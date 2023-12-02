n, m = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

j = 1
for i in range(n):
    if i == 0 or i == n-1:
        print("Yes")
    else:
        if T[j] == S[i]:
            print("Yes")
            j += 1
            # if j >= m - 1:
            #     j == m - 1
        else:
            print("No")

    
