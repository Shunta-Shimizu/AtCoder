h1, w1 = map(int, input().split())
A = []
for _ in range(h1):
    a = list(map(int, input().split()))
    A.append(a)

h2, w2 = map(int, input().split())
B = []
for _ in range(h2):
    b = list(map(int, input().split()))
    B.append(b)

Ah = []
for i in range(1<<h1):
    new = []
    tf = True
    for j in range(h1):
        if 1 & (i>>j) == 1:
            new.append(A[j])
    Ah.append(new)

B_t = list((zip(*B)))

for a in Ah:
    a_t = list((zip(*a)))
    # print("-------")
    # print(a_t)
    for i in range(1<<len(a_t)):
        ans = []
        for j in range(len(a_t)):
            if 1 & (i>>j) == 1:
                ans.append(a_t[j])
        # print("-----------")
        # print("ans", ans)
        # print("B_t", B_t)
        if ans == B_t:
            print("Yes")
            exit()

print("No")