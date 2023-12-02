n = int(input())

bit_n = bin(n)[2:] # 先頭の0bを取り除く　type=str

x = [""]
for i in reversed(bit_n):
    new_x = []
    if i == "0":
        for a in x:
            new_x.append("0"+a)
    else:
        for a in x:
            new_x.append("0"+a)
            new_x.append("1"+a)
    # print(new_x)
    x = new_x

x.sort()

for ans in x:
    print(int(ans, 2))