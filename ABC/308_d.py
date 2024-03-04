from collections import deque
h, w = map(int, input().split())
S = []
for _ in range(h):
    s = input()
    S.append(s)

snk = ["s", "n", "u", "k", "e"]
now = (0, 0)
que = deque()
que.append(now)
nodes = {now}
while que:
    x = que.popleft()
    i, j = x
    for k, si in enumerate(snk):
        if S[i][j] == si:
            if i+1 < h:
                if S[i+1][j] == snk[(k+1)%5]:
                    if (i+1, j) not in nodes:
                        nodes.add((i+1, j))
                        que.append((i+1, j))
            if i-1 >= 0:
                if S[i-1][j] == snk[(k+1)%5]:
                    if (i-1, j) not in nodes:
                        nodes.add((i-1, j))
                        que.append((i-1, j))               
            if j+1 < w:
                if S[i][j+1] == snk[(k+1)%5]:
                    if (i, j+1) not in nodes:
                        nodes.add((i, j+1))
                        que.append((i, j+1))
            if j-1 >= 0:
                if S[i][j-1] == snk[(k+1)%5]:
                    if (i, j-1) not in nodes:
                        nodes.add((i, j-1))
                        que.append((i, j-1))

if (h-1, w-1) in nodes:
    print("Yes")
else:
    print("No")