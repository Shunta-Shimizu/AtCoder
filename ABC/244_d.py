s1, s2, s3 = map(str, input().split())
t1, t2, t3 = map(str, input().split())

if s1 == t1:
    if s2 == t2:
        print("Yes")
    else:
        print("No")
else:
    if s2 == t2:
        print("No")
    else:
        if s3 == t3:
            print("No")
        else:
            print("Yes")