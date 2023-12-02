from collections import defaultdict, deque
n = int(input())
S = list(input())

cf = defaultdict(list)
que = deque()
keep = ""
ans = ""
for i in range(n):
    if S[i] == "(":
        cf[i] = -1
        que.appendleft(i)
    elif S[i] == ")":
        if len(que) == 0:
            cf[i] = -1
        else:
            q = que.popleft()
            cf[q] = i
            cf[i] = q
    else:
        cf[i] = -1

ans = []
for i in range(n):
    if S[i] == ")":
        if cf[i] != -1:
            c = i
            while c >= cf[i]:
                if ans[-1] == "(":
                    ans.pop(-1)
                    break
                else:
                    ans.pop(-1)
                    c -= 1
        else:
            ans.append(S[i])
    else:
        ans.append(S[i])

# print(cf)
print(*ans, sep="")