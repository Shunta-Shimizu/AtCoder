h, w = map(int, input().split())

A = []
for _ in range(h):
    A.append(list(map(int, input().split())))

tf = True
for i1 in range(h):
    for j1 in range(w):
        for i2 in range(i1, h):
            for j2 in range(j1, w):
                if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
                    continue
                else:
                    tf = False

if tf:
    print("Yes")
else:
    print("No")