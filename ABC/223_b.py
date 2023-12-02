S = input()

S_shift = [S]
for i in range(len(S)):
    S_f = S[0]
    S_rest = S[1:]
    S = S_rest + S_f
    S_shift.append(S)

for j in range(len(S)):
    S_l = S[-1]
    S_rest = S[:-1]
    S = S_l + S_rest
    S_shift.append(S)

# print(min(S_shift))
# print(max(S_shift))
S_shift.sort()
print(S_shift[0])
print(S_shift[-1])
