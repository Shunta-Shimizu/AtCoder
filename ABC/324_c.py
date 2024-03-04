n, Td = map(str, input().split())
n = int(n)
S = []
for _ in range(n):
    s = input()
    S.append(s)

ans = []
for i, s in enumerate(S):
    if abs(len(Td)-len(s)) > 1:
        continue
    else:
        if len(s)+1 == len(Td):
            cnt1 = 0
            for j in range(len(Td)):
                if s[j] != Td[j]:
                    break
                cnt1 += 1
                if j+1 == len(s):
                    # cnt1 += 1
                    break
            cnt2 = 0
            for j in range(len(Td)):
                if s[-(j+1)] != Td[-(j+1)]:
                    break
                cnt2 += 1
                if j+1 == len(s):
                    # cnt2 += 1
                    break
            if cnt1+cnt2 >= len(Td)-1:
                ans.append(i+1)
            # print(i+1, s, cnt1, cnt2)
        elif len(s) == len(Td)+1:
            cnt1 = 0
            for j in range(len(Td)):
                if s[j] != Td[j]:
                    break
                cnt1 += 1
            cnt2 = 0
            for j in range(len(Td)):
                if s[-(j+1)] != Td[-(j+1)]:
                    break
                cnt2 += 1
            # print(i+1, s, cnt1, cnt2)
            if cnt1+cnt2 >= len(Td):
                ans.append(i+1)
        elif len(s) == len(Td):
            cnt = 0
            for j in range(len(Td)):
                if s[j] != Td[j]:
                    cnt += 1
            if cnt <= 1:
                ans.append(i+1)

print(len(ans))
print(*ans)