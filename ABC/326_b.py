n = int(input())

for num in range(n, 920):
    if int(str(num)[0]) * int(str(num)[1]) == int(str(num)[2]):
        print(num)
        break