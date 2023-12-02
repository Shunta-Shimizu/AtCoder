S = input()

S_list = list(S)
a_count = 0

for i, s in enumerate(S_list):
    if s == "a":
        a_count = i+1

if a_count == 0:
    print(-1)
else:
    print(a_count)