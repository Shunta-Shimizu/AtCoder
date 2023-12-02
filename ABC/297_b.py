from collections import defaultdict
S = list(input())

tf_1 = False
tf_2 = False

S_dict = defaultdict(list)
for i in range(len(S)):
    S_dict[S[i]].append(i)

if (S_dict["B"][0] % 2 == 0 and S_dict["B"][1] % 2 != 0) or (S_dict["B"][0] % 2 != 0 and S_dict["B"][1] % 2 == 0):
    tf_1 = True

if S_dict["R"][0] < S_dict["K"][0] < S_dict["R"][1]:
    tf_2 = True

if tf_1 and tf_2:
    print("Yes")
else:
    print("No")

