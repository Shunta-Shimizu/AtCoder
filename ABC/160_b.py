x = int(input())

happy1 = x // 500 * 1000
happy2 = ((x - 500 * (x // 500)) // 5 ) * 5

print(happy1 + happy2)
