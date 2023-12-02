X = list(input())

if int(X[0]) == int(X[1]) == int(X[2]) == int(X[3]):
    print("Weak")
elif int(X[1]) - 1 == int(X[0]) and int(X[2]) - 1 == int(X[1]) and int(X[3]) - 1 == int(X[2]):
    print("Weak")
elif int(X[0]) == 9 and int(X[1]) == 0:
    if int(X[2]) + 1 == int(X[3]):
        print("Weak")
    else:
        print("Strong")
elif int(X[1]) == 9 and int(X[2]) == 0:
    if int(X[0]) == 8 and int(X[3]) == 1:
        print("Weak")
    else:
        print("Strong")
elif int(X[2]) == 9 and int(X[3]) == 0:
    if int(X[0]) == 7 and int(X[1]) == 8:
        print("Weak")
    else:
        print("Strong")
else:
    print("Strong")
