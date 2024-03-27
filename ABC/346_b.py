w, b = map(int, input().split())

ans = "wbwbwwbwbwbw"*100000


for i, ai in enumerate(ans):
    wc = 0
    bc = 0
    if ai == "w":
        wc += 1
        for j in range(1, w+b):
            if i+j >= len(ans):
                break
            if ans[i+j] == "w":
                wc += 1
            else:
                bc += 1
        if wc == w and bc == b:
            print("Yes")
            exit()

    else:
        bc += 1
        for j in range(1, w+b):
            if i+j >= len(ans):
                break
            if ans[i+j] == "w":
                wc += 1
            else:
                bc += 1
        if wc == w and bc == b:
            print("Yes")
            exit()

print("No")

