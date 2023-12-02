n, m = map(int, input().split())
s = list(input())
t = list(input())
# print(t[:len(s)])
# print(t[-(len(s)):])
if s == t[:len(s)] and s == t[-(len(s)):]:
    print(0)
elif s == t[:len(s)] and s != t[-(len(s)):]:
    print(1)
elif s != t[:len(s)] and s == t[-(len(s)):]:
    print(2)
elif s != t[:len(s)] and s != t[-(len(s)):]:
    print(3)