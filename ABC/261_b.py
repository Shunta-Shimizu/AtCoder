n = int(input())

match = []
for _ in range(n):
    result = input()
    match.append(result)

for i in range(n):
    for j in range(n):
        if i == j:
            if match[i][j] != "-":
                print("incorrect")
                exit()
        else:
            if match[i][j] == "W":
                if match[j][i] != "L":
                    print("incorrect")
                    exit()
            elif match[i][j] == "D":
                if match[j][i] != "D":
                    print("incorrect")
                    exit()
            else:
                if match[i][j] == "L":
                    if match[j][i] != "W":
                        print("incorrect")
                        exit()

print("correct")
