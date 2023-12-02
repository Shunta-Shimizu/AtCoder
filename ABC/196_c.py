n = input()

# x = 0
# ans = 0
# while x <= n:
#     if len(str(x)) % 2 != 0:
#         x = 10 ** len(str(x))
#     else:
#         # if list(str(x))[:len(str(x))//2] == list(str(x))[len(str(x))//2:]:
#         if x // (10 ** (len(str(x))//2)) == x % (10 ** (len(str(x))//2)):
#             ans += 1
#         x += 1

# print(ans)

n_f = int(n) // (10**(len(n)//2))
n_l = int(n) % (10**(len(n)//2))
ans = 0
for i in range(1, n_f+1):
    num = str(i)+str(i)
    if len(num) % 2 == 0:
        if int(num) <= int(n):
            ans += 1

print(ans)