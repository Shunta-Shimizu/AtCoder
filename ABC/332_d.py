h, w = map(int, input().split())
A = []
for _ in range(h):
    a = list(map(int ,input().split()))
    A.append(a)

B = []
for _ in range(h):
    b = list(map(int, input().split()))
    B.append(b)

for bit_i in range(1 << h):
    if str(bit_i).count("1") == 2:
        for i, bi in enumerate(str(bit_i)):
            swap = []
            if bi == "1":
                swap.append(i)
        tmp = A[swap[0]]
        A[swap[0]] = A[swap[1]]
        