n, m = map(int, input().split())

C = []
A_list = []
num_set = set()
for _ in range(m):
    c = int(input())
    A = list(map(int, input().split()))
    # num_set = num_set | set(A)
    C.append(c)
    A_list.append(A)

# print(num_set)
# l_num_set = sorted(list(num_set))
l_num_set = list(i+1 for i in range(n))
# print(l_num_set)
ans = 0
for bit in range(1, 1 << m):
    n_set = set()
    for i in range(m):
        if 1 & (bit >> i):
            n_set = n_set | set(A_list[i])
    l_n_set = sorted(list(n_set))
    # print(l_n_set)
    if l_n_set == l_num_set:
        ans += 1

print(ans)


