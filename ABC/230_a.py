n = int(input())

if n < 10:
    print("AGC00" + str(n))
elif n >= 42:
    print("AGC0" + str(n + 1))
else:
    print("AGC0" + str(n))

