S = input()

count = len(S)
zero_count = 0
for num in list(S):
    if num != "0":
        zero_count = 0
    elif num == "0" and zero_count == 0:
        zero_count = 1
    elif num == "0" and zero_count == 1:
        count -= 1
        zero_count = 0

print(count)

