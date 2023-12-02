from collections import defaultdict
n, m = map(int, input().split())

S = []
P = []
tf = defaultdict(bool)
wa_count = defaultdict(int)
for _ in range(m):
    p, s = map(str, input().split())
    S.append(s)
    P.append(int(p))
    tf[int(p)] = False
    wa_count[int(p)] = 0

ac_num = 0
for i in range(m):
    if S[i] == "AC":
        if tf[P[i]]:
            continue
        else:
            tf[P[i]] = True
            ac_num += 1
    else:
        if tf[P[i]]:
            continue
        else:
            wa_count[P[i]] += 1

wa_sum = 0
for k, v in tf.items():
    if v:
        wa_sum += wa_count[k]

print(ac_num, wa_sum)