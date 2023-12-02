H, W = map(int, input().split())

S = []
ssharp_count = []
for _ in range(H):
    s = list(map(str, input()))
    ssharp_count.append(s.count("#"))
    S.append(s)

T = []
tsharp_count = []
for _ in range(H):
    t = list(map(str, input()))
    tsharp_count.append(t.count("#"))
    T.append(t)

if ssharp_count == tsharp_count:
    print("Yes")
else:
    print("No")