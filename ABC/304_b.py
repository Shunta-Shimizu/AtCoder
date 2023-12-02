n = int(input())

# if n <= 10**3-1:
# elif 10**3 <= n <= 10**4-1:
# elif 10**4 <= n <= 10**5-1:
# elif 10**5 <= n <= 10**6-1:
# elif 10**6 <= n <= 10**7-1:
# elif 10**7 <= n <= 10**8-1:
# elif 10**8 <= n <= 10**9-1:

l = len(str(n))
if l < 3:
    print(n)
else:
    ans = int(n // 10**(l-3))
    ans2 = str(ans) + "0"*(l-3)
    print(ans2)