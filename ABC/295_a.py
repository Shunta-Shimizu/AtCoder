n = int(input())
W = list(map(str, input().split()))

tf = False

if "and" in W or "not" in W or "that" in W or "the" in W or "you" in W:
    tf = True

if tf:
    print("Yes")
else:
    print("No")