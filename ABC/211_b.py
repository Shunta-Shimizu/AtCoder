S1 = input()
S2 = input()
S3 = input()
S4 = input()

S_set = {S1, S2, S3, S4}
S_true = {"H", "2B", "3B", "HR"}

if len(S_set) == len(S_true):
    print("Yes")
else:
    print("No")