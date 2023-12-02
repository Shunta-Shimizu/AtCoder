n = int(input())
S = list(input())

for i, s in enumerate(S):
    if s == "1":
        if i % 2 == 0:
            print("Takahashi")
            exit()
        else:
            print("Aoki")
            exit()

