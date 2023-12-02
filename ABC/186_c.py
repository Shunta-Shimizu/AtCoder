n = int(input())

ans = 0
for i in range(1, n+1):
    i_set = set(list(str(i)))
    oct_i = set(list(oct(i)[2:]))

    if "7" not in i_set and "7" not in oct_i:
        ans += 1

print(ans)



