n = int(input())
B = list(map(int, input().split()))

ans = [B[0], B[-1]]
for i in range(n-2):
    ans.append(min(B[i], B[i+1]))

print(sum(ans))