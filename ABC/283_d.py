S = input()

word = ""
f_idx = []

for i in range(len(S)):
    if S[i] == "(":
        f_idx.append(len(word))
        continue
    elif S[i] == ")":
        # for s in S[f_idx+1:i]:
        #     if s in str_set:
        #         str_set.remove(s)
        word = word[:f_idx[-1]]
        f_idx.pop(-1)
    else:
        if S[i] in word:
            print("No")
            exit()
        word += S[i]
    # print(word)
print("Yes")

