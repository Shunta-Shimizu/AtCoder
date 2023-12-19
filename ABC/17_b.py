X = input()

tf = True
for i, x in enumerate(X):
    if i < len(X)-1:
        if x == "c":
            if X[i+1] != "h":
                tf = False
        else:
            if x == "h":
                if i == 0:
                    tf = False
                else:
                    if X[i-1] != "c":
                        tf = False
            else:
                if x not in ["o", "k", "u"]:
                    tf = False
    else:
        if x not in ["o", "k", "u"]:
            tf = False

if tf:
    print("YES")
else:
    print("NO")