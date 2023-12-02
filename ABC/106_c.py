S = input()
k = int(input())

if len(S) == 1:
    print(S)
else:
    if S[0] == "1":
        count = 0
        for s in S:
            if s == "1":
                count += 1
            else:
                break
        if count >= k:
            print("1")
        else:
            print(S[count])
    else:
        print(S[0])