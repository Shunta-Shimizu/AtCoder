S =  list(map(int, input().split()))

s0 = S[0]
for i in range(1, len(S)):
  if S[i] >= s0 and 100 <= S[i] <= 675 and S[i] % 25 == 0:
    s0 = S[i]
    continue
  else:
    print("No")
    exit()

print("Yes")  