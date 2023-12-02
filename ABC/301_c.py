from collections import defaultdict
S = list(input())
T = list(input())

cards = {"a", "t", "c", "o", "d", "e", "r"}
dict_s = defaultdict(int)
dict_t = defaultdict(int)
dict_s["@"] = 0
dict_t["@"] = 0
for i in range(len(S)):
    dict_s[S[i]] = 0
    dict_s[T[i]] = 0
    dict_t[S[i]] = 0
    dict_t[T[i]] = 0

for i in range(len(S)):
    dict_s[S[i]] += 1
    dict_t[T[i]] += 1

for k, v in dict_s.items():
    if k != "@":
        if dict_s[k] == dict_t[k]:
            continue
        elif dict_s[k] < dict_t[k]:
            if k in cards and dict_s["@"] > 0:
                dict_s["@"] -= dict_t[k] - dict_s[k]
                if dict_s["@"] < 0:
                    print("No")
                    exit()
            else:
                print("No")
                exit()
        elif dict_s[k] > dict_t[k]:
            if k in cards and dict_t["@"] > 0:
                dict_t["@"] -= dict_s[k] - dict_t[k]
                if dict_t["@"] < 0:
                    print("No")
                    exit()
            else:
                print("No")
                exit()               
print("Yes")