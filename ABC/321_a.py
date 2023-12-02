N = input()

if len(N) == 1:
    print("Yes")
else:
    tf = True
    tmp = int(N[0])
    for n in N[1:]:
        if tmp > int(n):
            tmp = int(n)
        else:
            tf = False
    if tf:
        print("Yes")
    else:
        print("No")

