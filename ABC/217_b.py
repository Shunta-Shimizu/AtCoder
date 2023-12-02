s1 = input()
s2 = input()
s3 = input()

s_list = [s1, s2, s3]
contest = ["ABC", "ARC", "AGC", "AHC"]

for c in contest:
    if c not in s_list:
        print(c)
        exit()