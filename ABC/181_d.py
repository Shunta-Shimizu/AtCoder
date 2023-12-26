from collections import defaultdict
S = input()

count = defaultdict(int)
hachi = set()
num = 0
i = 1
while True:
    num = 8*i
    if num < 1000:
        hachi.add(num)
    else:
        break
    i += 1

for s in S:
    count[s] += 1

for n in hachi:
    tf = True
    check = defaultdict(int)
    if len(S) >= 3:
        if len(str(n)) >= 3:
            for i, si in enumerate(str(n)):
                if count[si]-check[si] > 0:
                    check[si] += 1
                else:
                    tf = False
            if tf:
                print("Yes")
                exit()
    else:
        if len(S) == 1:
            if int(S)%8 == 0:
                print("Yes")
                exit()
        elif len(S) == 2:
            if int(S)%8 == 0:
                print("Yes")
                exit()
            elif int(S[1]+S[0])%8 == 0:
                print("Yes")
                exit()

print("No")