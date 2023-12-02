n = int(input())
S =  list(input())

count = 0
idx = []
for i in range(n):
    if S[i] == '"':
        count += 1
        if count == 1:
            continue
        elif count == 2:
            count = 0

    elif S[i] == "," and count == 0:
        S[i] = "."
    elif S[i] == "," and count == 1:
        S[i] = "."
        idx.append(i)

for j in idx:
    S[j] = ","
    
print(*S, sep="")