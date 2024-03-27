n = int(input())
S = input()
C = list(map(int, input().split()))

LC = []
for i, s in enumerate(S):
    if i == 0:
        LC.append([s, 1])
    else:
        if LC[-1][0] == s:
            LC[-1][1] += 1
        else:
            LC.append([s, 1])
    
count = 0
for i, lc in enumerate(LC):
    if lc[1] == 2:  # 修正: lc[1]が2のときにカウントを増やす
        count += 1

if count <= 1:
    print(0)


