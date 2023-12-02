n = int(input())
S = input()

for i in range(1, n):
    l = 0
    for j in range(n-i):
        if S[j] == S[j+i]:
            break
        else:
            l += 1
    print(l)