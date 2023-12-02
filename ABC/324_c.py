from collections import defaultdict
n, Td = map(str, input().split())
n = int(n)
S = []
for _ in range(n):
    s = input()
    S.append(s)


ans = []
for i in range(n):
    count = 0
    if len(S[i]) < len(Td):
        for j in range(len(Td)):
            if count > 2:
                break
            else:
                if S[i][j] != Td[j+count]:
                    count += 1
    elif len(S[i]) > len(Td):
        for j in range(len(Td)):
            if count > 2:
                break
            else:
                if S[i][j] != Td[j+count]:
                    count += 1
    else:
        for j in range(len(Td)):
            if count > 2:
                break
            else:
                if S[i][j] != Td[j]:
                    count += 1
    print(count)

print(ans)
