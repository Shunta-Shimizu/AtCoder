import itertools
S = input()
pin = {1:3, 2:2, 3:4, 4:1, 5:3, 6:5, 7:0, 8:2, 9:4, 10:6}

count = [0]*7

for i, s in enumerate(S):
    if s == "1":
        count[pin[i+1]] += 1

split_judge = 0

for l, r in itertools.combinations(range(7), r=2):
    if count[l] >= 1 and count[r] >= 1:
        for k in range(l+1, r):
            if count[k] == 0:
                split_judge = 1

if split_judge == 1 and S[0] == "0":
    print("Yes")
else:
    print("No")