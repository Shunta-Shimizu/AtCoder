N = int(input())

S_list = []
for _ in range(N):
    S = str(input())
    S_list.append(S)

if len(set(S_list)) != len(S_list):
    print("No")
    exit()

firsr_str = {"H", "D", "C", "S"}
second_str = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
count = 0
for s in S_list:
    s_split = list(s)
    if (s_split[0] in firsr_str) and (s_split[1] in second_str):
        count += 1

if count == N:
    print("Yes")
else:
    print("No")