a, b, c, d, e = map(int, input().split())
card_list = [a, b, c, d, e]
cards = {a, b, c, d, e}

card1 = 0
card2  = 0
if len(cards) == 2:
    if card_list.count(a) == 2 or card_list.count(a) == 3:
        print("Yes")
    else:
        print("No")

else:
    print("No")