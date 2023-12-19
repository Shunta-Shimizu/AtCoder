from collections import defaultdict, deque
n = int(input())
S = input()

Lque = deque()
Rque = deque()
Rque.append(0)
for i, s in enumerate(S):
    if s == "L":
        Rque.appendleft(i+1)
    else:
        pre = Rque.popleft()
        Lque.append(pre)
        Rque.appendleft(i+1)

ans = []
while Lque:
    ans.append(Lque.popleft())

while Rque:
    ans.append(Rque.popleft())

print(*ans)
