k = int(input())

hour = k // 60
minutes = k % 60

if minutes < 10:
    time = str(21 + hour) + ":" + "0" + str(minutes)
else:
    time = str(21 + hour) + ":" + str(minutes)

print(time)